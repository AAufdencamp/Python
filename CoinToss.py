# Write your code below this line 👇
#You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
#There are many ways of doing this. But to practice what we learnt in the last lesson, 
#you should generate a random number, either 0 or 1. Then use that number to print out "Heads" or "Tails".
# Hint: Remember to import the random module first. 🎲

###MyCode##
import random
coin = [0,1]
toss = random.choice(coin)

#print(toss)

if toss == 0:
  print("Heads")
else:
  print("Tails")

#####InstructorCode###
import random

random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")