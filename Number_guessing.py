# Below are the steps:
#
# Build a Number guessing game, in which the user selects a range.
# Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
# Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses

import random
import math


def guess_the_number(min_range=int(input("Please insert a first number: ")),
                     max_range=int(input("Please insert a second number, higher than the first one: "))):
    generated_number = random.randint(min_range, max_range)
    print(generated_number)

    print("\n\tYou've only got ",
          round(math.log(max_range - min_range + 1, 2)),
          "chances to guess the number!\n")

    guessed_number = int(input(f"Guess the number between {min_range} and {max_range}: "))
    counter = 1
    while guessed_number in range(min_range, max_range + 1):
        if guessed_number < generated_number:
            print("Try again! You guessed to low.")
            counter += 1
            guessed_number = int(input("Insert a higher number: "))
            if counter >= math.log(max_range - min_range + 1, 2):
                print(f"The correct number is {generated_number}.")
                print("Better luck next time! :)")
                break
            continue
        elif guessed_number > generated_number:
            print("Try again! You guessed to high.")
            guessed_number = int(input("Insert a lower number: "))
            counter += 1
            if counter >= math.log(max_range - min_range + 1, 2):
                print(f"The correct number is {generated_number}.")
                print("Better luck next time! :)")
                break
            continue
        elif guessed_number == generated_number:
            print(f"Congratulations! You guessed the correct number in {counter} tries.")
            break




guess_the_number()