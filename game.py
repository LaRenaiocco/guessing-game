"""A number-guessing game."""
import random
# keeps track of score for each game
scores = []

def greet_player():
    # greet player
    print("Hello friend.  Are you ready to play a guessing game?")
    # get player name
    name = input("What is your name?  ")
    print(f"Nice to meet you, {name}.")
    print("Now lets play.  You'll have 7 tries to guess the correct number")

def play_game():
    # choose a random number
    num = random.randint(1,100)
    guess_count = 0
    guesses_remaining = 7
    # repeat the following
    while guesses_remaining > 0:
    # have player guess a number
        user_num = input("Guess a number between 1 and 100 > ")
        #check user input is integer
        try:
            user_num = int(user_num)
        except:
            print("That is not a number. Please try again.")
            continue
        # Loop to correct if guess is correct
        # number is too high
        if user_num > num:
            print("That is incorrect")
            print("Lower!")
            guess_count += 1
            guesses_remaining -= 1
            print(f"You have {guesses_remaining} guesses remaining.")
        # number is too low    
        elif user_num < num:
            print("That is incorrect")
            print("Higher!")
            guess_count += 1
            guesses_remaining -= 1
            print(f"You have {guesses_remaining} guesses remaining.")
        # number is correct
        elif user_num == num:
            print("That is correct! You win!")
            print(f"You guessed the number in {guess_count} tries.")
            #add this games score to the scores list
            scores.append(guess_count)
            #check for best overall score
            best_score = min(scores)
            print(f"Your best score is {best_score}")
            break

def play_again():
    print("Would you like to play again? (Y)es or (N)o?")
    play_again = input(" > ")
    if play_again.upper() == "Y":
        print("Great, let's play again.")
        return True
    else:
        print("Thanks for playing, goodbye!")
        return False
        

def complete_game():
    greet_player()
    while True:
        play_game()
        play_again_choice = play_again()
        if play_again_choice == False:
            break


complete_game()

