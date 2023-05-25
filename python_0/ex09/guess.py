#!/usr/bin/python3
import random
import os
"""
You have to make a program that will be an interactive guessing game.
It will ask the user to guess a number between 1 and 99.

"""

min_secret = 1
max_secret = 99
"""
The program will tell the user if their input is too high or too low.

The game ends when the user finds out the secret number or types exit.

You will import the random module with the randint function to get a random
number.

You have to count the number of trials and print that number when the user
wins.
"""


def welcome():
    os.system('clear')
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 ", end="")
    print("to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")
    print()


def secret_42():
    if secret == 42:
        print("The answer to the ultimate question of life,")
        print("the universe and everything is 42A")
        print("Congratulations! You got it on your first try!")


def you_guessed(counter: int):
    if counter == 1:
        print("Fantastic guess. You win at first try")
        secret_42()
    else:
        print("Congratulations, you've got it!")
        print("You won in {} attempts!".format(counter))


def treat_guess(guess: int, counter: int) -> bool:
    guessed = False
    if guess == secret:
        you_guessed(counter)
        guessed = True
    elif guess > secret:
        print("Too high!")
    else:
        print("Too low!")
    return guessed


secret = random.randint(min_secret, max_secret)


welcome()
guessed = False
counter = 0

while not guessed:
    guess_txt = input("What's your guess between 1 and 99? ").strip()

    if guess_txt.isnumeric():
        counter = counter + 1      # counting good trials
        guessed = treat_guess(int(guess_txt), counter)
    elif guess_txt.lower() == "exit":
        print("Goodbye!")
        guessed = True
    else:
        print("That's not a number")
        counter = counter + 1      # counting bad trials
