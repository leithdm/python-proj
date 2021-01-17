
import random
import hangman_words
import hangman_art

stages = hangman_art.stages
game_over = False
lives = 6
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

print(hangman_art.logo)
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

