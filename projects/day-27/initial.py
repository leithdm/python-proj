# ARGS
# Unlimited Positional Arguments in a function
# using (*args) for an undefined number of arguments
# args are stored in a tuple
def add(*args):
    print(type(args))
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(12, 12, 12, 12, 12, 12, 12))

# KWARGS
# Unlimited Key Word arguments
# kwargs are stored in a dictionary
def calculate(**kwargs):
    print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    # print(kwargs["add"])

def calculate_2(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]

calculate(add=3, multiply=5)
calculate_2(2, add=3, multiply=5)


# BASICS OF TKINTER
# TKINTER was ported over from tk. In order to make it work, alot of the arguemnts
# were replaced with **kwargs, which is why we don't see the properties appear when
# hovering over the method()

# to illustrate this, lets create our own class

class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]

        # get an error when instantiating if DONT have a .get().
        # By using kw.get() will just return None if dont specify when instantiating
        #this is perfect for lots of optional key word arguments
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.make)

# below will crash if we DONT use self.make = kw.get("make")
my_car = Car(make="Nissan")



# import tkinter
# import turtle
#
# t = turtle.Turtle()
# t.write()
# window = tkinter.Tk()
# window.title("GUI")
# window.minsize(width=500, height=300)
# my_label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
#
# # label will not show without pack functionality
# my_label.pack(side="left")
# window.mainloop()