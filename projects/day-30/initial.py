# try
# except - do this if there was an exception
# else
# finally - always exectuted, doesnt matter what happens

# 1. Basic example
# try:
#     file = open("test.txt")
# except:
#     file = open("test.txt", "w")
# else:
#     print("all good")
# finally:
#     print("fuck off")

# 2. Slightly more elaborate example
# try:
#     file = open("test.txt")
#
# except FileNotFoundError:
#     file = open("test.txt", "w")
#     file.write("foobar")
# # can get hold of the error message by using 'as' error_foo-bar
# except KeyError as error_message:
#     file = open(f"{error_message} does not exist")
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     file.close()
#     print("file was closed")

# 3. Raising your own exception
# try:
#     file = open("test.txt")
#
# except FileNotFoundError:
#     file = open("test.txt", "w")
#     file.write("foobar")
# # can get hold of the error message by using 'as' error_foo-bar
# except KeyError as error_message:
#     file = open(f"{error_message} does not exist")
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     raise KeyError
#     raise TypeError("This is an error I made up")

# 4. Another example of raising own exceptions
# height = float(input("Height: "))
# weight = float(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human height not over 3m")
#
# bmi = weight / height**2
# print(bmi)

# Challenge 1
fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")

make_pie(4)

# Challenge 2
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        # total_likes += 0  ...better just to use pass
        pass
    else:
        print(total_likes)