import datetime as dt
import math
import tkinter

from data_provider import DataProvider
from email_sender import EmailSender

INFO_FONT = ("Calibri", 12)
OBSERVER_LAT = 34.234234
OBSERVER_LONG = 123.277367
OBSERVER_Y = 360 - int(OBSERVER_LAT + 90) * 2
OBSERVER_X = int(OBSERVER_LONG + 180) * 2


class MapDisplay:

    def __init__(self, data_provider: DataProvider, email_service: EmailSender):
        self.data_provider = data_provider
        self.email_service = email_service
        self.window = tkinter.Tk()
        self.window.title("ISS Tracker")
        self.window.config(bg="white")
        self.canvas = tkinter.Canvas(width=720, height=360, bg="white")
        map_image = tkinter.PhotoImage(file="images/map.png")
        rocket_image = tkinter.PhotoImage(file="images/rocket.png")
        observer_image = tkinter.PhotoImage(file="images/observer.png")
        sun_image = tkinter.PhotoImage(file="images/sun.png")
        self.map = self.canvas.create_image(360, 180, image=map_image)
        self.rocket = self.canvas.create_image(360, 180, image=rocket_image)
        self.observer = self.canvas.create_image(OBSERVER_X, OBSERVER_Y, image=observer_image)
        self.sun = self.canvas.create_image(360, 180, image=sun_image)
        self.canvas.grid(row=1, column=0, columnspan=3)

        self.geographical_info = tkinter.Label(text="Geographical Info", bg="white", fg="black", font=INFO_FONT)
        self.geographical_info.grid(row=0, column=0)
        self.time_info = tkinter.Label(text="Time Info", bg="white", fg="black", font=INFO_FONT)
        self.time_info.grid(row=0, column=1)
        self.observation_status = tkinter.Label(text="Observation Status", bg="white", fg="black", font=INFO_FONT)
        self.observation_status.grid(row=0, column=2, pady=20)

        self.run_the_show()

        self.window.mainloop()

    def run_the_show(self):
        sunrise_h, sunset_h, now_h = self.data_provider.get_time_data()
        is_dark_enough = sunrise_h >= now_h or sunset_h <= now_h
        now = dt.datetime.now().strftime("%d/%m/%Y %H:%M")
        self.time_info.config(text=f"Current time\n{now}")
        if is_dark_enough:
            self.when_dark()
            self.window.after(30000, self.run_the_show)
        else:
            till_dark = sunset_h - now_h
            self.when_light(till_dark)
            self.window.after(3600000 * till_dark, self.run_the_show)

    def when_dark(self):
        self.show_images(True)
        self.show_sun(False)
        lat, long = self.data_provider.get_iss_position()
        self.geographical_info.config(text=f"ISS position\nLongitude: {long}\nLatitude: {lat}")
        lat = self.position_parsing("lat", lat)
        long = self.position_parsing("long", long)
        self.canvas.moveto(self.rocket, long, lat)
        is_close_enough = self.distance() < 10
        if is_close_enough:
            self.email_service.send_email()
            self.observation_status.config(text="Night is upon us\nTime for watching!")
        else:
            self.observation_status.config(text="Night is upon us\nWe have to wait...")

    def when_light(self, till_dark):
        self.show_images(False)
        self.show_sun(True)
        lat, long = self.data_provider.get_iss_position()
        self.geographical_info.config(text=f"ISS position\nLongitude: {long}\nLatitude: {lat}")
        self.observation_status.config(text="Sun is blinding us!!!")
        self.time_info.config(text=f"Waiting for the night\n{till_dark} hours till dark")

    def show_images(self, are_visible):
        if are_visible:
            state = "normal"
        else:
            state = "hidden"
        self.canvas.itemconfig(self.rocket, state=state)
        self.canvas.itemconfig(self.observer, state=state)

    def show_sun(self, is_visible):
        if is_visible:
            state = "normal"
        else:
            state = "hidden"
        self.canvas.itemconfig(self.sun, state=state)

    @staticmethod
    def position_parsing(type_of_coordinate: str, coordinate_value: int) -> int:
        if type_of_coordinate == "lat":
            return 360 - int(coordinate_value + 90) * 2
        elif type_of_coordinate == "long":
            return int(coordinate_value + 180) * 2
        else:
            return 0

    def distance(self) -> int:
        rocket_coordinates = self.canvas.coords(self.rocket)
        observer_coordinates = self.canvas.coords(self.observer)
        distance = math.dist(rocket_coordinates, observer_coordinates)
        return int(distance)
