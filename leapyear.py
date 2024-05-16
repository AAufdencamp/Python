# Which year do you want to check? INSTRUCTOR CODE
year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")


year = int(input()) MY CODE
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
  if year % 100 != 0:
    print("Leap year")
  elif year % 400 == 0:
    print("Leap year")
  else:
    print("Not leap year")
else:
  print("Not leap year")