import json
import string  # collection of characters
from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox  # must be imported separately from tkinter import *

import bcrypt  # allows the use of hashing
import pandas as pd
import pandastable as pt  # allows to create a GUI table from a pandas DataFrame
import pyperclip  # allows to copy plaintext to the system clipboard
from cryptography.fernet import Fernet  # allows to use Fernet encryption/decryption capabilities

# Colors
RED = "#d4483b"
DARK_RED = "#bd2814"
DARK_GREY = "#474747"
GREY = "#878484"
CREAM = "#f5f9e3"

# Fonts
FONT1 = ("Roboto", 9, "bold")
FONT2 = ("Arial", 9, "normal")

# Logo
LOGO = "logo.png"

# Characters
CHARACTERS = {
    "letters": string.ascii_lowercase + string.ascii_uppercase,
    "numbers": string.digits,
    "symbols": list(filter(lambda char: char not in "(){}[]|~ ,'=+-", string.punctuation))
}

# Starting Keys
key_1 = ""
key_2 = ""


# ---------------------------- ACCESS KEY SETUP ------------------------------- #
def access_key_setup():
    """Creates a window for the user to set up an access key the first time he opens the program. This key will be
    saved to the hashed_key.txt file and used for subsequent accesses to the program. This key must be 32 bytes long
    and will be hashed using bcrypt hashing before being stored. Once the key is created allows the user to access
    the main program window."""
    global key_1
    global key_2
    key_1 = password_input1.get().encode('utf-8')
    key_2 = confirmation_input.get().encode('utf-8')

    # Check if the two keys entered by the user match and return an error if they don't
    if key_1 != key_2:
        messagebox.showerror(title='Non-matching keys',
                             message='The two encryption keys entered do not match. Please enter matching keys.')
    # Check if the entered key is 32 bytes long and raise error if it is not
    elif len(key_1) != 32:
        messagebox.showerror(title='Key length error',
                             message='The encryption key entered is not 32 bytes long. Please enter a key comprising '
                                     '32 alphanumeric characters.')
    # If the two keys match and are the right length then we will save a hash of the key and open the main window
    else:
        hashed_key = bcrypt.hashpw(password=key_1, salt=bcrypt.gensalt())  # Create hashed key
        hashed_key = hashed_key.decode('utf-8')
        with open('hashed_key.txt', mode='w') as key_file:
            key_file.write(hashed_key)

        # Close the key creation window and open the main window
        starting_window.destroy()
        window.deiconify()


# ---------------------------- ACCESS KEY CHECK ------------------------------- #
def access_key_check():
    """On subsequent accesses to the program this funtion is triggered to prompt the user to enter the access key he
    created previously. If the access key matches the stored key inside the hashed_key.txt file then allows the user to
    proceed to the main program window."""
    global key_1
    key_1 = password_input2.get().encode('utf-8')
    with open('hashed_key.txt', mode='r') as key_file:
        hashed_key = key_file.read()
        hashed_key = hashed_key.encode('utf-8')

    # Check if the key matches the saved key and if correct then open the main window
    if bcrypt.checkpw(key_1, hashed_key):
        starting_window.destroy()
        window.deiconify()
    # If key is incorrect then raise error
    else:
        messagebox.showinfo(title='Incorrect Key', message="Your access key is incorrect. Please try again.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Creates a random password containing both symbols and alphanumeric characters. Quantity of letters can vary
    between 8 or 10 (uppercase and lowercase characters). Quantity of numbers and symbols can vary between 2 and 4.
    Copies the generated password to the system clipboard."""
    password_entry.delete(0, END)
    # add random number of letters between 8 - 10
    password_list = [choice(CHARACTERS["letters"]) for _ in range(randint(8, 10))]
    # add random number of numbers between 2 - 4
    password_list += [choice(CHARACTERS["numbers"]) for _ in range(randint(2, 4))]
    # add random number of symbols between 2 - 4
    password_list += [choice(CHARACTERS["symbols"]) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = ''.join(password_list)  # ''.join() concatenates each character inside password_list and forms a string
    password_entry.insert(END, password)
    pyperclip.copy(password)  # copy password to systems clipboard


# ---------------------------- GENERATE FERNET KEY ------------------------------- #
def generate_fernet_key():
    """Creates an encryption key to be used with the Fernet encryption library during encryption and decryption tasks.
    Stores the generated key in the 'fernet_key.key' file."""
    # key generation
    key = Fernet.generate_key()

    # store key in file
    with open('fernet_key.key', 'wb') as f:
        f.write(key)


# ---------------------------- LOAD FERNET KEY ------------------------------- #
def load_fernet_key():
    """Reads and returns the stored Fernet encryption key from the 'fernet_key.key' file."""
    with open('fernet_key.key', 'rb') as f:
        key = f.read()
    return key


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Saves to data.json the information relative to Site, Username and Password provided by the user (Password
    information is encrypted using Fernet encryption before being stored). Gives user confirmation via a messagebox."""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo("Empty Fields", "Please fill in all the required fields.")
    else:
        fernet = Fernet(load_fernet_key())  # instance of Fernet(), uses fernet key

        # encrypt password information. To be able to encrypt we must encode first
        encrypted_password = fernet.encrypt(password.encode())

        # format data to be stored, in this case, as a dictionary. We must decode encrypted_password to be able to save
        # it as text instead as byte
        data = {
            website: {
                "username": email,
                "password": encrypted_password.decode()
            }
        }

        # we can't update the content of data.json file directly, so first we read the current content and store it in a
        # dictionary called current_content_dict
        try:
            # we try to read the file and get the current_content_dict
            with open("data.json", "r") as f:
                current_content_dict = json.load(f)
        except FileNotFoundError:
            # if the file was not found we create it and store the data
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        else:
            # if the file was found we get the current_content_dict and update it with the new data
            current_content_dict.update(data)
            # finally we overwrite data.json with the updated info
            with open("data.json", "w") as f:
                json.dump(current_content_dict, f, indent=4)
        finally:
            # give user confirmation
            messagebox.showinfo("Password Saved", "Your password was correctly saved \nand copied to the clipboard.")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- VIEW PASSWORDS ------------------------------- #
def view():
    """Creates a new window to view the information relative to Sites, Usernames and Passwords currently stored in
    data.json file."""
    fernet = Fernet(load_fernet_key())  # instance of Fernet(), uses fernet key

    # we read the data inside the data.json file and for each item we separate the website name, username and
    # password information and store them individually on separate variables. We also decrypt and decode the
    # password information. Finally, we create a new list called content_as_list where each element of the list is a
    # list with the three variables. This list will be used to create a DataFrame later
    try:
        with open('data.json', 'r') as f:
            file_content = json.load(f)
    except FileNotFoundError:
        with open("data.json", "w") as f:
            json.dump({}, f, indent=4)
        messagebox.showinfo("File Not Found Error", "File 'data.json' was not found. File has been created.")
    else:
        content_as_list = []
        for website, website_info in file_content.items():
            site = website
            username = website_info["username"]
            password = fernet.decrypt(website_info["password"]).decode()
            content_as_list.append([site, username, password])

        # create DataFrame from content_as_list
        columns = ["Site", "Email", "Password"]
        df = pd.DataFrame(content_as_list, columns=columns)

        # create view_passwords_window
        view_passwords_window = Toplevel(window)
        view_passwords_window.title('Password Viewer')
        view_passwords_window.geometry('600x350')
        view_passwords_window.config(padx=20, pady=20)

        # create a pandastable passing both the window and DataFrame created before
        table = pt.Table(view_passwords_window, dataframe=df)
        options = {'fontsize': 10, 'cellbackgr': CREAM, 'textcolor': DARK_GREY}
        pt.config.apply_options(options, table)
        table.editable = False  # makes pandastable not editable
        table.show()

    # TODO: 1. Allow to edit the pandastable inside the view_passwords_window to modify any data the user wants and once
    #  the window is closed (or either via some button) allow to save the updated info back to data.json file. This
    #  implies taking all the info inside the table, encrypt the passwords, format the info and overwrite data.json. The
    #  'View Saved Passwords' button should now say 'View / Edit Saved Passwords'. Same with the message inside the
    #  instructions_label on the main window; it should now say 'You can Save and View/Edit your saved passwords with
    #  the buttons down below.'"""


# ---------------------------- SEARCH PASSWORDS (redundant, just for fun) ------------------------------- #
def search():
    site = website_entry.get()
    if len(site) == 0:
        messagebox.showinfo("Empty Field", "Please provide a website name for the search.")
    else:
        try:
            with open("data.json", "r") as f:
                content = json.load(f)
        except FileNotFoundError as error_message:
            messagebox.showinfo("File Not Found Error", "No Data File Found.")
        else:
            # fernet = Fernet(load_fernet_key())
            # try:
            #     content[site]
            # except KeyError:
            #     messagebox.showinfo("Search Result", f"The website '{site}' is not in your saved passwords.")
            # else:
            #     site_name = site
            #     username = content[site]["username"]
            #     password = fernet.decrypt(content[site]["password"]).decode()
            #     message = f"Website: {site_name}\nUsername: {username}\nPassword: {password}"
            #     messagebox.showinfo("Search Result", message)
            if site in content:
                fernet = Fernet(load_fernet_key())
                site_name = site
                username = content[site]["username"]
                password = fernet.decrypt(content[site]["password"]).decode()
                message = f"Website: {site_name}\nUsername: {username}\nPassword: {password}"
                messagebox.showinfo("Search Result", message)
            else:
                messagebox.showinfo("Search Result", f"The website '{site}' is not in your saved passwords.")


# ---------------------------- MAIN UI SETUP ------------------------------- #
# Main User interface accessed once authenticated. Allows User to create and store passwords.

# Window
window = Tk()
window.title("MyPass Manager")
window.resizable(False, False)
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file=LOGO)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
instructions_message = ("Welcome to MyPass Manager!\n\nThe best place to generate Secure Password for your sites ;) "
                        "\n\nYou can Save and View your saved passwords with the buttons down \nbelow but only You "
                        "can see your information as it is securely encrypted \nbefore being stored. Be secure and "
                        "enjoy using MyPass Manager.")
# instructions_message = ("MyPass Manager It's your Ultimate Password Companion!\n\nExperience the Power to Save and View"
#                         " your Passwords \nat Your Fingertips. \n\nYour Data, Your Control – Guarded by Fortified "
#                         "Encryption🔐\n\nEnter your details below and start using MyPass \nManager, your Digital "
#                         "Fortress! 🏰")

instructions_label = Label(text=instructions_message, font=FONT1, fg=DARK_GREY)
instructions_label.grid(column=0, columnspan=3, row=1, pady=(0, 10))
website_label = Label(text="Website:", font=FONT1, fg=DARK_GREY)
website_label.grid(column=0, row=2, sticky=W)
email_label = Label(text="Email/Username:", font=FONT1, fg=DARK_GREY)
email_label.grid(column=0, row=3, sticky=W)
password_label = Label(text="Password:", font=FONT1, fg=DARK_GREY)
password_label.grid(column=0, row=4, sticky=W)

# Entries
website_entry = Entry(font=FONT2, bg=CREAM)
website_entry.grid(column=1, row=2, columnspan=2, sticky=EW, pady=3)
website_entry.focus()
email_entry = Entry(font=FONT2, bg=CREAM)
email_entry.grid(column=1, row=3, columnspan=2, sticky=EW, pady=1)
# email_entry.insert(0, "felipemunozri@gmail.com")
email_entry.insert(0, "example@mail.com")
password_entry = Entry(font=FONT2, bg=CREAM, show="●")
password_entry.grid(column=1, row=4, sticky=EW)

# Buttons
generate_button = Button(text="Generate", command=generate_password, font=FONT2, bg=RED, fg=CREAM,
                         activebackground=DARK_RED, activeforeground=CREAM, relief=RAISED, borderwidth=1, width=13)
generate_button.grid(column=2, row=4, padx=(2, 0), pady=2)
save_button = Button(text="Save Password", command=save, font=FONT2, bg=RED, fg=CREAM, activebackground=DARK_RED,
                     activeforeground=CREAM, relief=RAISED, borderwidth=1)
save_button.grid(column=1, row=5, columnspan=2, sticky=EW)
# search functionality is redundant, evaluate removing it
# search_button = Button(text="Search Password", command=search, font=FONT2, bg=RED, fg=CREAM,
#                        activebackground=DARK_RED, activeforeground=CREAM, relief=RAISED, borderwidth=1)
# search_button.grid(column=1, row=6, columnspan=2, sticky=EW, pady=2)
view_button = Button(text="View Saved Passwords", command=view, font=FONT2, bg=RED, fg=CREAM,
                     activebackground=DARK_RED, activeforeground=CREAM, relief=RAISED, borderwidth=1)
view_button.grid(column=1, row=7, columnspan=2, sticky=EW, pady=2)

# ---------------------------- ACCESS SETUP UI ------------------------------- #
# Starting User interface. First time prompts user to create a global access key. Subsequent accesses asks for user's
# access key.

# Starting Window
starting_window = Toplevel()
starting_window.resizable(False, False)
starting_window.title("MyPass Manager")
starting_window.config(padx=40, pady=40)

# Detect if the user has already set up an access key. If the user has never opened the program, the
# 'hashed_key.txt' file will be blank and the program will request that the user establish an access key.
while True:
    try:
        with open("hashed_key.txt", mode="r") as file:
            contents = file.read()
    except FileNotFoundError:
        with open("hashed_key.txt", mode="w") as file:
            file.write("")
            continue
    else:
        break
if contents == "":  # Check if no encryption key has been created
    # Canvas
    starting_canvas = Canvas(starting_window, height=200, width=200, highlightthickness=0)
    logo_image_2 = PhotoImage(file=LOGO)
    starting_canvas.create_image(100, 100, image=logo_image_2)
    starting_canvas.grid(column=0, row=0)

    # Labels
    welcome_label = Label(starting_window, text='Welcome to MyPass Manager!', font=FONT1, fg=DARK_GREY)
    welcome_label.grid(row=1, column=0, pady=(0, 10))
    welcome_message = ("Please set up an access Key \nfor the application.\n\nThis key "
                       "must be exactly 32 bytes long \n(i.e. 32 ') alphanumeric characters & simple symbols).\n "
                       "You should make the key easy to remember by,\nfor example, using a sequence of random "
                       "words.\n\nBe aware that if you lose the key there is\nno means to recover it.")
    request_label = Label(starting_window, text=welcome_message, font=FONT2, fg=DARK_GREY)
    request_label.grid(row=2, column=0, pady=(0, 10))

    confirmation_label = Label(starting_window, text="Please re-enter your key:", font=FONT2, fg=DARK_GREY)
    confirmation_label.grid(row=4, column=0, pady=(0, 10))

    # Entries
    password_input1 = Entry(starting_window, font=FONT2, show="●", bg=CREAM)
    password_input1.grid(row=3, column=0, pady=(0, 10), ipadx=40)
    confirmation_input = Entry(starting_window, font=FONT2, show="●", bg=CREAM)
    confirmation_input.grid(row=5, column=0, pady=(0, 10), ipadx=40)

    # Button
    enter_button = Button(starting_window, text="Enter", command=access_key_setup, font=FONT2, bg=RED, fg=CREAM,
                          activebackground=DARK_RED, activeforeground=CREAM, relief=RAISED, borderwidth=1, width=8)
    enter_button.grid(row=6, column=0, pady=(0, 10))

    # TODO: 2. Check if Fernet Key exist first and then create it if not. Same with data.json file. Evaluate possibility
    #  to add an import option at start for both files so users can migrate their data from one instance of MyPass
    #  Manager to another
    # Generate Fernet Key first time we open the program
    generate_fernet_key()

    # Create empty data.json file first time we open the program
    with open('data.json', 'r') as f:
        file_content = json.load(f)


# If an encryption key has been created
else:
    login_label = Label(starting_window, text="MyPass Access", font=FONT1, fg=DARK_GREY)
    login_label.grid(row=0, column=0)
    key_label = Label(starting_window, text="Please type your access key below \nto enter the application:",
                      font=FONT2, fg=DARK_GREY)
    key_label.grid(row=1, column=0, pady=5)

    password_input2 = Entry(starting_window, font=FONT2, show="●", bg=CREAM)
    password_input2.grid(row=2, column=0, pady=5, ipadx=40)
    password_input2.focus()

    login_button = Button(starting_window, text="Access", command=access_key_check, font=FONT2, bg=RED,
                          fg=CREAM,
                          activebackground=DARK_RED, activeforeground=CREAM, relief=RAISED, borderwidth=1, width=8)
    login_button.grid(row=3, column=0, pady=10)

window.withdraw()  # Hides the main window until the correct encryption key is entered
window.mainloop()
