# 1. Basic format for list comprehension
# new_list = [NEW_ITEM for ITEM in LIST], where we replace the KEY_WORDS
# numbers = [1, 2, 3]
# new_numbers = [n+1 for n in numbers] ..... [2, 3, 4]

# 2. Conditional List comprehension
# new_list = [NEW_ITEM for ITEM in LIST if TEST]
# names = ['darren', 'jim', 'eleanor']
# new_list_4 = [n for n in names if len(n) < 4]
# new_list_5 = [n.upper() for n in names]

# one solution
file1_list = list(open("file1.txt", "r"))
# print(file1_list.readlines())

file2_list = list(open("file2.txt", "r"))
# print(file2_list.readlines())

new_list = [int(i) for i in file1_list for j in file2_list if i == j]
print(set(new_list))

# second solution - better
with open("file1.txt") as file1:
    # convert to a list
    file1_data = file1.readlines()

with open("file2.txt") as file2:
    file2_data = file2.readlines()

result = [int(num) for num in file1_data if num in file2_data]
print(result)

# 3. Dictionary Comprehension
# new_dict = {new_key: new_value for item in list}
# import random
# new_dict = {n:random.randrange(1, 100) for n in names}

# CREATE new dictionary based on values in existing dict
# new_dict = {new_key: new_value for (key, value) in dict.items() if CONDITION}
# NOTE: TAKE NOTE OF THE dict.ITEMS() method called on the dict !
# passed_students = {k:v for (k,v) in new_dict.items() if v >= 60}

# Exercise 1
# sentence = "What is the Airspeed Velocity of an Unladen Swallow"
# words = sentence.split()
# result = {word:len(word) for word in words}

# Exercise 2
# weather_c = {
#     "Monday": 12,
#     "Tuesday":14,
#     "Wednesday": 16
# }
# weather_f = {k:(v*9/5 + 32) for (k, v) in weather_c.items() }

# Exercise 3
# Using pandas, DataFrame, iterrow() to get row data from a DataFrame
# student_dict = {
#     "student" : ["Harry", "Hermione"],
#     "score": [12, 12]
# }
# for (index, row) in student_data_frame.iterrows():
#     if row['student'] == 'Harry':
#         print(row['score'])
#