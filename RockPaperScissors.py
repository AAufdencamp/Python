rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#####MY-CODE#############
# #Write your code below this line 👇
# import random
# plays = [rock, paper, scissors]
# computer_play = random.choice(plays)
# guest_play = input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

# if guest_play == "0":
#     print(f"Computer plays: {computer_play}")
#     if computer_play == plays[0]:
#         print("It's a draw")
#     if computer_play == plays[1]: 
#         print("You lose. Paper beats rock")
#     if computer_play == plays[2]:
#         print("You win! Rock beats scissors")

# if guest_play == "1":
#     print(f"Computer plays: {computer_play}")
#     if computer_play == plays[0]:
#         print("You win! Paper beats rock")
#     if computer_play == plays[1]: 
#         print("It's a draw.")
#     if computer_play == plays[2]:
#         print("You lose. Scissors beat paper.")

# if guest_play == "2":
#     print(f"Computer plays: {computer_play}")
#     if computer_play == plays[0]:
#         print("You lose. Rock beats scissors")
#     if computer_play == plays[1]: 
#         print("You win! Scissors beat paper.")
#     if computer_play == plays[2]:
#         print("It's a draw.")

# ####INSTRUCTOR-CODE with My Debugging########
# import random

# game_images = [rock, paper, scissors]
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
# #recall that input() always returns a string
# computer_choice = random.randint(0,2)

# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number, you lose!")
# else:
#     print(game_images[user_choice])
#     print(f"Computer chose:")
#     print(game_images[computer_choice])
    
#     if user_choice == 0 and computer_choice == 2:
#         print("You win!")
#     elif computer_choice == 0 and user_choice ==2:
#         print("You lose.")
#     elif computer_choice > user_choice:
#         print("You lose")
#     elif user_choice > computer_choice:
#         print("You win!")    
#     elif computer_choice == user_choice:
#         print("It's a draw.")

#####InstructorCode######
import random

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
#recall that input() always returns a string
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0,2)
    print(f"Computer chose:")
    print(game_images[computer_choice])
    
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice ==2:
        print("You lose.")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")    
    elif computer_choice == user_choice:
        print("It's a draw.")
    