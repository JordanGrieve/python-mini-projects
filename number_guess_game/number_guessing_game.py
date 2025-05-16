import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# A function to check users' guess vs actual answer
def check_answer(user_guess, answer, turns):
    """Checks answer against guess, returns the number of turns left"""
    if user_guess > answer:
        print("User guess is too high.")
        return turns - 1
    elif user_guess < answer:
        print("User guess is too low.")
        return turns - 1
    else:
        print(f"You got it! the answer was {answer}")

# Function to see difficulty
def game_level():
    game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if game_level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    # Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"ppstt the answer is: {answer}")


    turns = game_level()

    user_guess = 0

    while user_guess != answer:
        print(f"You have {turns} attempt remaining to guess the number.")
        # Let the user guess the number
        user_guess = int(input("Make a guess: "))
        turns = check_answer(user_guess, answer, turns)
        if turns == 0:
            print("You've run out guesses. You lose.")
            return
        elif user_guess != answer:
            print("Guess again.")

game()





