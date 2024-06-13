from replit import clear
from art import logo



#Calculator

#add
def add(n1, n2):
  return n1 + n2

#subtract
def subtract(n1, n2):
  return n1 - n2  
  
#multiply
def multiply(n1, n2):
  return n1 * n2  
  
#divide
def divide(n1, n2):
  return n1 / n2  



#create a dictionary where the keys are the symbols and the values are the names of the functions
operations = {
              "+": add,
             "-": subtract,
             "*": multiply,
             "/": divide,
}

#this dictionary, operations, is going to be the means by which we will call the functions for the calculator operators

#function = operations["*"]
#print(function(2,3))


#we define a recursive function that will allow the user to provide a fresh input if they do not want to continue with #the current calculation "thread". A recursrive function is a function that calls itself. It has no inputs or outputs.
#def caclulator():

# num1 = int(input("What's the first number?: "))

# for symbol in operations:
#   """we loop through the dictionary and print out the keys. Recall that the keys are the symbols"""
#   print(symbol)

# operation_symbol = input("Pick an operation from the line above: ")

# num2 = int(input("What's the second number?: "))

# calculation_function = operations[operation_symbol]


# first_answer = calculation_function(num1, num2)
  
# print(f"{num1} {operation_symbol} {num2} = {first_answer}")

# #difference between print() to console and return a function output
# #we can pass in an output from a previous function, ie the variable answer or even as the function call itself, as the input for the next function
# #We want to code this program so that we can keep calculating with the previous answer as long as the user chooses
# should_continue = True
###My CODE####
# while should_continue:
#   user_choice = input(f"Type 'y' to continue calculating or type 'n' to exit.: ")
#   if user_choice == 'n':
#     print(f"Goodbye")
#     should_continue = False
#   elif user_choice == 'y':
#     operation_symbol = input("Pick another operation: ")
#     next_num = int(input("What's the next number?: "))
#     calculation_function = operations[operation_symbol]
#     next_answer = calculation_function(first_answer, next_num)
#     print(f"{first_answer} {operation_symbol} {next_num} = {next_answer}")
#     first_answer = next_answer
###End My Code###

def calculator():
  print(logo)

  #converting to floats so that we can use decimals or whole numbers.
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator() #here we call the recursive function calculator() to allow user to enter fresh input if they type 'n'

calculator()      