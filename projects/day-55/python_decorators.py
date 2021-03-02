# Advanced python decorators

# class User:
#     def __init__(self, username):
#         self.username = username
#         self.is_logged_in = False
#
#
# def is_authenticated_user(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             function(args[0])
#     return wrapper
#
#
# @is_authenticated_user
# def create_blog_post(user):
#     print(f"Blog post created by {user.username}")
#
#
# new_user = User('darren')
# new_user.is_logged_in = True
# create_blog_post(new_user)


# Logging Decorator
# Create a logging_decorator() which is going to log the name of the function that was
# called, the arguments it was given and finally the returned output.

def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}{args}")
        result = function(args[0], args[1], args[2])
        print(f"It returned: {result}")
    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a+b+c

a_function(1, 2, 3)