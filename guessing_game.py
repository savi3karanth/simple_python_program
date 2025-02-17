import random
from guess_game_art import logo


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        print("You have 10 attempts remaining to guess the number")
        return 10
    else:
        print("You have 5 attempts remaining to guess the number")
        return 5


def game():
    print(logo)

    print("Welcome to the Number guessing game")
    print("I am thinking of a number from 1 to 100")
    answer = random.randint(1, 100)
    print(f"The correct answer is {answer}")
    turns = set_difficulty()
    guess = 0

    while turns > 0:
        print(f"You have {turns} attempts to guess")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print(f"You have run out of guesses. The answer was {answer}")
            break
        elif guess != answer:
            print("Guess again")

game()
