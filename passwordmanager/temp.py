import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

# password_letters = [random.choice(letters) for i in range(nr_letters)] #list comprehension for a range!
# password_symbols = [random.choice(symbols) for i in range(nr_symbols)] #list comprehension for a range!
# password_numbers = [random.choice(numbers) for i in range(nr_numbers)] #list comp for a range

passletter = []
for item in range(random.randint(8, 10)):
    passletter.append(random.choice(letters))



print(passletter)
    # print(item)
    # print(type(item))
    # passletter = []
    # item = random.choice(letters)
    # passletter.append(item)



# print(passletter)
# print(len(passletter))
#
# print(len(range(random.randint(8,10))))
# print(range(random.randint(8,10)))
