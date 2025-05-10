from art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game! ")

print(r"I'm thinking of a number between 1 and 100.")

number_to_guess=random.randint(1,100)


def difficulty_level(diff):
    if diff == "easy":

        c=10
        return c
    else:
        c=5
        return c

difficulty=input(r"Choose a difficulty. Type 'easy' or 'hard': ")

attempt=difficulty_level(difficulty)

is_continue=False

while attempt>0:
    print(f"You have {attempt} attempts remaining to guess the number")
    user_guess=int(input("Make a guess: "))
    if number_to_guess == user_guess:
        print("You won!!")
        break
    elif number_to_guess < user_guess:
        print("Too High")

    elif number_to_guess > user_guess:
        print("Too Low")

    attempt -= 1

    if attempt==0:
        print("You've run out of guesses. You lose 😢")
        print(f"The number was {number_to_guess}.")
    else:
        print("Guess again...")