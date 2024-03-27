def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)


add(1, 2, 3, 4)


def calculation(n, **kwargs):
    s = n + kwargs["add"]
    m = n + kwargs["mult"]
    print(s)
    print(m)


calculation(1, add=2, mult=3)

class Car:

    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.make = kw.get("make")  # when we use .get() if the parameter wasn't specified it returns None intead of crashing
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car =  Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)



my_car2 =  Car(make="Toyota")
print(my_car2.make)
print(my_car2.model)
