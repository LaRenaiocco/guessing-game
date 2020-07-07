"""A number-guessing game."""
import random
# greet player
print("Hello friend.  Are you ready to play a guessing game?")
# get player name
name = input("What is your name?  ")
print(f"Nice to meet you, {name}.")
# choose a random number
def play_game():
    num = random.randint(1,100)
    guess_count = 0
    # repeat
    while True:
    # have player guess a number
        user_num = input("Guess a number between 1 and 100 > ")
        #check user input is integer
        try:
            user_num = int(user_num)
        except:
            print("That is not a number. Please try again.")
            continue
    # Loop to correct if guess is correct
        if user_num > num:
            print("That is incorrect")
            print("Lower!")
            guess_count += 1
        elif user_num < num:
            print("That is incorrect")
            print("Higher!")
            guess_count += 1
        elif user_num == num:
            print("That is correct! You win!")
            print(f"You guess the number in {guess_count} tries.")
            break
play_game()
