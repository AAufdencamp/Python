# fruits = ["apple", "peach", "pear"]
# for i in range(len(fruits)):
#   print(fruits[i])
# print("\n")


# fruit = ["Raspberry", "Blackberry", "Blueberry"]
# for fruit in fruit:
#   print(fruit)
#   print(fruit + " Pie\n")
# print(fruit)

###Using For Loops with range()####
for i in range(1,11,3): #this ranges excludes the last number. Since I want to print 1 thru 10 I will set the range to 11.
  print(i)            #the third argument in range() is the step.

total = 0
for i in range(1,101):
  total += i
print(total)