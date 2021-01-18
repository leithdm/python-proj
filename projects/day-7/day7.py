
import random
from hangman_words import word_list
from hangman_art import logo, stages

game_over = False
lives = 6
chosen_word = random.choice(word_list)

print(logo)
print(f"Debug: Chosen word is {chosen_word}")
display = []
for _ in chosen_word:
    display += "_"

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}.")

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = guess
    print(display)
    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print("You Lose. Game Over")
            game_over = True

    if "_" not in display:
        print("You win!")
        game_over = True

    print(stages[lives])

