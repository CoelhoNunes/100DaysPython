import tkinter


# def add(*args):
#     print(args[0])
#     print(sum(args))
#
#
# add(1, 2, 3, 5, 6, 8)
#

def cal(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


cal(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.make)
print(my_car.colour)
