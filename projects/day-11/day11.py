import random
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_random_card():
    return random.choice(cards)

def get_score(user_cards):
    total = 0
    for value in user_cards:
        total += value
    return total

def blackjack():
    play_game = True
    while play_game:
        continue_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n")
        if continue_playing == 'y':
            check_for_another_card = True
            user_cards = [get_random_card(), get_random_card()]
            print(user_cards)
            user_score = get_score(user_cards)
            computers_cards = [get_random_card(), get_random_card()]
            computer_score = get_score(computers_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computers_cards[0]}")

            if user_score == 21:
                print(f"Your final hand: {user_cards}, final score: {user_score}")
                print("BLACKJACK - You win!")  
                check_for_another_card = False       

            while check_for_another_card:
                user_input = input("Type 'y' to get another card, type 'n' to pass:\n")
                if user_input == 'y':
                    user_cards.append(get_random_card())
                    user_score = get_score(user_cards)
                    print(f"Your cards: {user_cards}, current score: {user_score}")
                    if user_score > 21:
                        print(f"Bust ! Game Over")
                        check_for_another_card = False
                elif user_input == 'n':
                    print(computer_score)
                    computer_score = get_score(computers_cards)
                    if computer_score  > user_score:
                        print(f"Your final hand: {user_cards}, final score: {user_score}")
                        print(f"Computer's final hand: {computers_cards}, final score: {computer_score}")
                        print("You lose")
                        check_for_another_card = False   
                    elif computer_score == user_score:
                        print(f"Your final hand: {user_cards}, final score: {user_score}")
                        print(f"Computer's final hand: {computers_cards}, final score: {computer_score}")
                        print("It's a draw!")      
                        check_for_another_card = False   
                    else: 
                        while computer_score < user_score:
                            print(f"in the nasty block {computer_score}")
                            computers_cards.append(get_random_card())    
                            computer_score = get_score(computers_cards)
                            if computer_score > 21:
                                print(f"Your final hand: {user_cards}, final score: {user_score}")
                                print(f"Computer's final hand: {computers_cards}, final score: {computer_score}")
                                print("You win!")  
                                check_for_another_card = False   
                            elif computer_score == user_score:
                                print(f"Your final hand: {user_cards}, final score: {user_score}")
                                print(f"Computer's final hand: {computers_cards}, final score: {computer_score}")
                                print("It's a draw!")  
                                check_for_another_card = False
                            else:
                                print(f"Your final hand: {user_cards}, final score: {user_score}")
                                print(f"Computer's final hand: {computers_cards}, final score: {computer_score}")
                                print("You lose")
                                check_for_another_card = False                                           
        elif continue_playing == 'n':
            play_game = False
            
blackjack()




