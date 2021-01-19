import random

EASY_LIVES = 10
HARD_LIVES = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

target_number = random.randint(1, 100)

print(f"Debug: the number is {target_number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

num_lives = 0

if difficulty == 'easy':
    num_lives = EASY_LIVES
elif difficulty == 'hard':
    num_lives = HARD_LIVES

print(f"You have {num_lives} attempts remaining to guess the number.")

guess = int(input("Make a guess: "))

while guess is not target_number:
    if guess < target_number:
        num_lives -= 1
        print("Too low.")
        if num_lives == 0:
            print("You've run out of guesses. Game Over")
            break
        print("Guess again")
        print(f"You have {num_lives} attempts remaining to guess the number")

    elif guess > target_number:
        num_lives -= 1
        print("Too high.")
        if num_lives == 0:
            print("You've run out of guesses. Game Over")
            break
        print("Guess again")
        print(f"You have {num_lives} attempts remaining to guess the number")   

    guess = int(input("guess again: "))

if guess == target_number:
    print("You got it ! Well Done")   