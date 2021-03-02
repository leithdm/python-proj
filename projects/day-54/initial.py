# Understanding Decorator Function
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# function can take in another function as input
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


result = calculate(add, 5, 2)
print(result)


# function can have nested functions
# below, we are also returning a function
def outer_function():
    print("im outer")

    def nested_function():
        print("im inner")

    return nested_function


inner_function = outer_function()
inner_function()


# Decorator format
# FUNCTION that wraps another function and gives it additional functionality
def decorator_function(function):
    def wrapper_function():
        function()

    return wrapper_function()


# Example of a decorator
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
        print("i modify something")
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")

#With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")

#Without the @ syntactic sugar
def say_greeting():
    print("How are you?")

#Without the @ syntactic sugar calling method
# decorated_function = delay_decorator(say_greeting)
# decorated_function()

# Calling, with the syntactic sugar
say_bye()