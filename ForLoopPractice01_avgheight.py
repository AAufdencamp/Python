####ForLoopPractice01_MyCode#######
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
#goal: write at least one for loop (don't use len() or sum())

number_of_students = 0
height = 0

for i in student_heights:
  number_of_students += 1
  height += i

total_height = height
average_height = round((total_height / number_of_students))
print(f"total height = {total_height}")
print(f"number of students = {number_of_students}")
print(f"average height = {average_height}")

########InstructorCode#############
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Your code below this row 👇
total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")
