#Print logo of higher_lower game.

from art import logo,vs
from game_data import data
import random
from replit import clear

def format_data(account):
  """Takes the account data and returns the printable format."""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
  """Takes the user guess and follower counts and returns if they got it right."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"




#Display art
score = 0
game_should_continue = True
account_b = random.choice(data)



while game_should_continue:
  #Generater a random account from the game data.
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)

  #Format the account data into printable format.
  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")

  # Ask user for a guess.
  guess = input("Who has more followers? Type 'A' or 'B':").lower()

  # Check if user is correct.
  ## Get follower count on each account.
  a_follower_account = account_a["follower_count"]
  b_follower_account = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_account, b_follower_account)

  clear()
  print(logo)

  #Give user feedback on their guess.
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    game_should_continue == False
    print("Sorry, that's wrong")

  #Score keeping.

  #Make the game repeatable.

  # Making account at position B to become next account at position A.

  # Clear the screen between rounds.