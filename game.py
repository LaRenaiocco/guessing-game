"""A number-guessing game."""
import random
# greet player
print("Hello friend.  Are you ready to play a guessing game?")
# get player name
name = input("What is your name?  ")
print(f"Nice to meet you, {name}.")
# choose a random number
num = random.randint(1,100)
guess_count = 0
# repeat
while True:
# have player guess a number
    user_num = int(input("Guess a number between 1 and 100 > "))
# if number is incorrect give them  a hint
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
# too high or too low

# increase number of guesses
# if number is correct the player wins
