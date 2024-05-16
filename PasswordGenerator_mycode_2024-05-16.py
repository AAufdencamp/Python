#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_ops = [letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# print(type(random.choice(letters)))
# print(random.choice(letters))

# part1 = str()
# for i in range(0, 5):
#   print(random.choice(letters))
#   part1 += random.choice(letters)
# print(part1)  

letters_01 = str()
for i in range(0, (nr_letters)):
  letters_01 += random.choice(letters)
print(type(letters_01))  
print(letters_01)

symbols_01 = str()
for i in range(0, (nr_symbols)):
  symbols_01 += random.choice(symbols)
print(type(symbols_01))  
print(symbols_01)

numbers_01 = str()
for i in range(0, (nr_numbers)):
  numbers_01 += random.choice(numbers)
print(type(numbers_01))  
print(numbers_01)

password = letters_01 + symbols_01 + numbers_01
password = list(password)
print(password)
random.shuffle(password)
print(password)

final_pwd = str()
for i in range(0, len(password)):
  final_pwd += password[i]
print(final_pwd)  