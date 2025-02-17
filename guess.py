import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    level = input("Choose the difficulty Type 'easy' or 'hard'")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def check_answer(user_answer, actual_answer, turns):
    if user_answer > actual_answer:
        print("Too high")
        return turns - 1
    elif user_answer < actual_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it the correct answer is {actual_answer}")

def game():
    print("Welcome to guess the number game")
    print("I am thinking of number from 1 to 100")
    answer = random.randint(1, 100)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} guess the number again")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You lose you ran out of attempts")
            return
        elif guess != answer:
            print("guess again")

game()