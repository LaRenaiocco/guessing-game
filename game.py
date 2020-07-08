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
    # allow user to set range
    customize_range = input("Would you like to customize the range of numbers you'll be guessing between? (Y)es or (N)o? ")
    if customize_range.upper() == "Y":    
        low_num = int(input("Select a number for the start of the range. "))
        high_num = int(input("Select a number for the end of the range. "))
    else:
        low_num = 1
        high_num = 100
    # choose a random number
    num = random.randint(low_num,high_num)
    guess_count = 0
    guesses_remaining = 7
    # repeat the following
    while guesses_remaining > 0:
    # have player guess a number
        user_num = input(f"OK! Guess a number between {low_num} and {high_num} > ")
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
            print("Lower! Lower! Lower!")
            guess_count += 1
            guesses_remaining -= 1
            print(f"You have {guesses_remaining} guesses remaining.")
            if guesses_remaining == 0:
                print("You lose!")
        # number is too low    
        elif user_num < num:
            print("That is incorrect")
            print("Higher! Higher! Higher!")
            guess_count += 1
            guesses_remaining -= 1
            print(f"You have {guesses_remaining} guesses remaining.")
            if guesses_remaining == 0:
                print("You lose!")
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
        print("Thanks for playing!")
        return False

def play_computer():
    print("Would you like to play against the computer now? (Y)es or (N)o?")
    play_against_comp = input(" > ")
    play_against_comp = play_against_comp.upper()
    if play_against_comp == "Y":
        print("Ok! Now you get to play against the computer!")
        print("Let's set the range that the computer will guess within")
        low = int(input("What is the lowest number of the range? "))
        high = int(input("What is the highest number of the range?"))
        print(f"Now think of a number between {low} and {high}")
        while True:
            computer_guess = random.randint(low, high)
            print(f"The computer guesses {computer_guess}")
            player_response = input("Please enter \n [H] for too high \n [L] for too low \n [C] for correct!")
            player_response = player_response.upper()
            if player_response == "H":
                high = computer_guess
            elif player_response == "L":
                low = computer_guess
            elif player_response == "C":
                print("The computer always knows...")
                print("Thanks for playing!")
                break
            else:
                print("That was not a valid option...")
    else:
        print("Thanks for playing, Goodbye!")

        

def complete_game():
    greet_player()
    while True:
        play_game()
        play_again_choice = play_again()
        if play_again_choice == False:
            break
    play_computer()


complete_game()

