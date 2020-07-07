"""A number-guessing game."""
import random
# greet player
print("Hello friend.  Are you ready to play a guessing game?")
# get player name
name = input("What is your name?  ")
print(f"Nice to meet you, {name}.")
# choose a random number
num = random.randint(1,100)
print(num)
# repeat:
# have player guess a number
# if number is incorrect give them  a hint
# too high or too low
# increase number of guesses
# if number is correct the player wins
