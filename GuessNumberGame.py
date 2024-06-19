#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
# import random
# from art import logo
# print(logo)

# def winning_num():
#   winner = random.randint(1, 100)
#   return winner

# easy_count = 5
# hard_count = 10
# # def easy():
# #   for i in range(1,6):

# print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
# print(f"Psst, the correct answer is {winning_num()}")
# #choose_level = str(input("Choose a difficulty. Type 'easy' or 'hard':\n").lower)

# def pick():
#   if str(input("Choose a difficulty. Type 'easy' or 'hard':\n").lower) == 'easy':
#     print(f"You have 5 attempts remaining to guess the number.")
#   else:
#     print(f"You have 10 attempts remaining to guess the number.")

# pick()
######
from random import randint
from art import logo

print(logo)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5



def check_answer(guess, answer):
  if guess > answer:
    print("Too high.")
  elif guess < answer:
    print("Too low.")
  else:
    print(f"You got it: the answer was {answer}.\n")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == 'easy':
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
  

def game():
  print("Welcome to the guessing game.")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}")
  turns = set_difficulty()
  print(f"You have {turns} attempts remaining to guess the number.")
  
  guess = 0

  ##MY CODE####
  while guess != answer:
    guess = int(input("Make a guess: "))
    check_answer(guess, answer)
    if guess == answer:
      game()
    if turns > 0 and guess != answer:
      turns -= 1 
      if turns == 0:
        print("You lose.\n")
        game()
      else:
        print(f"You have {turns} attempts remaining to guess the number.")
   ####end MY CODE####       
  
game()



