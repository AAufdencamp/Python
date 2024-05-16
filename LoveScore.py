###My Code:

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
#lower() count()
count1 = 0
count2 = 0
true = ["t","r","u","e"]
love = ["l","o","v","e"]

for i in true:
  if name1.lower().count(i) > 0:
    count1 += (name1.lower().count(i))
  if name2.lower().count(i) > 0:
    count1 += (name2.lower().count(i))
print(count1)

for i in love:
  if name1.lower().count(i) > 0:
    count2 += (name1.lower().count(i))
  if name2.lower().count(i) > 0:
    count2 += (name2.lower().count(i))
print(count2)

lovescore = count1 + count2
print(lovescore)

if lovescore < 10 or lovescore > 90:
  print(f"Your score is {lovescore}, you go together like coke and mentos.")
elif lovescore >= 40 and lovescore <= 50:
  print(f"Your score is {lovescore}, you are alright together.")
else:
  print(f"Your score is {lovescore}.")  

###Not summing correctly####

##Intstructor Code
print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# Your code below this line 👇
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

lovescore = int(str(first_digit) + str(second_digit)) #not adding like in maths. we are combining the digits rather than adding. Concatenate.

#We wrap score inside int() so we can compare the score with numbers in our score analysis

if (lovescore < 10) or (lovescore > 90):
  print(f"Your score is {lovescore}, you go together like coke and mentos.")
elif (lovescore >= 40) and (lovescore <= 50):
  print(f"Your score is {lovescore}, you are alright together.")
else:
  print(f"Your score is {lovescore}.")  




