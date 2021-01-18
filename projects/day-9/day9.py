'''
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

student_grades = {}

def convert_score(grade):
    result = " "
    if grade >= 91:
        result += "Outstanding"
    elif grade >= 81:
        result += "Exceeds Expectation"
    elif grade >= 71:
        result += "Acceptable"
    else:
        result += "Fail"
    return result

for key in student_scores:
    value = convert_score(student_scores[key])
    student_grades[key] = value



# 🚨 Don't change the code below 👇
print(student_grades)



travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities
    travel_log.append(new_country)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

'''

from art import logo
print(logo)

bids = {}
bidding_finished = False

# def clear():


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Joe": 123, "Jim": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input(
        "Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
#   elif should_continue == "yes":
#     clear()


