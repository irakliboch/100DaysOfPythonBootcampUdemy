#Choosing a random number between 1 and 100
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns - 1
  else:
    print(f"You win! The answer was {answer}")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS





def game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  answer = randint(1,100)
  print(f"Pssst, the number is {answer}")

  #Make function to set diffuculty

  #Let user guess the number
  turns = set_difficulty()

  guess = 0

  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You ran out of attempts. You lose")
      return 
    elif guess != answer:
      print("Guess again")

game()
  #Check the number they guess against actual answer

  #Track the number of turns and reduce by 1 if it's wrong.


  #Repeat the guess functionality 








  #import random

  ##computer_choice = random.randint(1,101)
  #print(computer_choice)
  #user_choice = 0

  #while computer_choice != user_choice:
  # def play_game():
    #  user_choice = int(input("What is your choice?"))
    # print(user_choice)



#play_game()

