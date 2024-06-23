############DEBUGGING#####################

# Describe Problem
# '''as is the function iterates over a range and at a certain length it is supposed to print a statement, 
# but range() in Python excludes the max limit of the range. To fix the bug we increase the range by 1.'''
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug
# '''Sometimes the original code produces IndexError: list index out of range.
# Let us try to break the code so that is always produces this IndexError
# Okay, to do that we need to print(dice_imgs[6])
# Now lets fix the code so it never breaks. To do this we understand that randint() includes both end ranges
# and that lists in Python start the index at 0'''
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# #print(dice_imgs[dice_num])
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994: # the inclusive range is 1981 - 1993
#   print("You are a millenial.")
# elif year >= 1994: #to make this work it must be >= 1994. It must include 1994.
#   print("You are a Gen Z.")

# Fix the Errors
# '''As is the code generates TypeError:">" not supported btwn str and int. Use int() wrapped around input
# To print value of age in print statement, use f string
# To provide input for any age under 18, use and else statement:-)
# '''
# age = int(input("How old are you?"))
# if age > 18:
#   print(f"You can drive at age {age}.")
# else:
#   print(f"Sorry, {age} is too young to drive.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: ")) # == is looking for equivalency, not assignment
# total_words = pages * word_per_page
# #try printing the actual value of some of the variables for which there is input from the user
# print(f"pages = {pages}")
# print(f"word_per_page = {word_per_page}")
# print(total_words)

#Use a Debugger
#a_list = []
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
#the above code is fixed by me but the lesson is about using Debuggers
#https://pythontutor.com/render.html#mode=display
#We can insert a break point to tell the computer to stop at a certian point in the code so we can examine
#where something went wrong.
#to insert a breakpoint in Python Tutor click on the line of code and see that it turns red. That is your
#breakpoint. Use the scroll button to rewind Python Tutor back to the red mark on the scroll line
#inidicating that is where your breakpoint exists.

# Tip #7 --Take a Break:-)
# Tip #8 -- Run your program often after every execution.
# Tip #9 -- Stackoverflow

# Which number do you want to check?
# number = int(input())
# if number % 2 == 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

# # Error line 4: if number % 2 = 0:
# # Remember that single "=" is assignment.
# # Double "==" is checking for equality.


# year = int(input()) # TypeError without int() conversion

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")

# Target is the number up to which we count
target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number) # remove square brackets []

#Whereas if we have an elif statement,then at any point, it could end the if, elif, else loop once 
#it finds one of them to be true, so that's an early exit option and it's more efficient in most cases.
#In the case where the code had three if statements, then the function needs to check every single if statemnet!
#The flow of a conditional statement is very important thing to wrap your head around,
# and this is a good example of where it is crucial to use elif instead of if.