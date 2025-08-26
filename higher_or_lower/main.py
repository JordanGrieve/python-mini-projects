# Display art
from art import logo, vs
from game_data import data
import random
print(logo)
score = 0

account_b = random.choice(data)

def formate_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

game_should_continue = True

while game_should_continue:
    # Generate a radom account from the game data

    # Making account at position B becomes the next account at position A
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {formate_data(account_a)}.")
    print(vs)
    print(f"Against B: {formate_data(account_b)}.")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear screen
    print("\n" * 20)
    print(logo)

    # Check if user is correct
    ## Get follower count of each account
    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_followers_count, b_followers_count)

    ### use if statement to check if user is correct
    if is_correct:
        score += 1
        print(f"You got it! Current score is: {score}.")
    else:
        print(f"Sorry, that's wrong. Final Score: {score}")
        game_should_continue = False

# Give user feedback on their guess


