"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
Description : A fun game which allow user to guess the
              stored number with minimal tries.
Author      : Paul Raj
Date        : 13th February 2021

"""

import random
import sys

print(
    """
      ===============================
      WECLOME TO NUMBER GUESSING GAME
      ===============================
      """
)


def start_game(last_score=0):
    # function for handling user exit response
    def user_response(response):
        if response == "y":
            if last_score == 0:
                return start_game(guess_count)
            elif guess_count < last_score:
                start_game(guess_count)
            else:
                start_game(last_score)
        elif response == "n":
            print("\nGood Bye!")
            sys.exit()
        else:
            response = input("Wrong Input, Would you like to play again? Y/N :").lower()
            user_response(response)

    # code for number guessing game
    if last_score:
        print("\nYour Best Score is {}!\n".format(last_score))

    random_number = random.randrange(1, 10)
    guess_count = 1
    try:
        guessed_number = int(input("Please enter a Number between 1 - 10 : "))
        if guessed_number > 10 or guessed_number < 1:
            print("\nOut of Range, Please Choose Number between 1 and 10!\n")
            start_game(last_score)
    except ValueError:
        print("\nWrong Input, Please Enter an Integer between 1 and 10!\n")
        start_game(last_score)
    else:
        while True:
            if guessed_number > random_number:
                print("Entered Number is greater than guessed Number!")
                guessed_number = int(input("Out of range, Please enter a Number between 1 - 10 : "))
                guess_count += 1
                continue
            elif guessed_number < random_number:
                print("Entered Number is less than guessed Number!")
                guessed_number = int(input("Please enter a Number between 1 - 10 : "))
                guess_count += 1
                continue
            elif guessed_number == random_number:
                print("\nGuessed Number is correct!")
                break
        print("number of guesses are : {}\n".format(guess_count))
        response = input("Would you like to play again? Y/N :").lower()
        user_response(response)


# Game Kick Off
start_game()
