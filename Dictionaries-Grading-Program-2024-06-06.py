###Dictionaries-GradingProgram###

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grade = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

####MY CODE###

for key in student_scores:
  if student_scores[key] <= 70:
    student_grade[key] = "Fail"
  elif student_scores[key] <= 80:
    student_grade[key] = "Acceptable"
  elif student_scores[key] <= 90:
    student_grade[key] = "Exceeds Expectations"
  else:  
    student_grade[key] = "Outstanding"

###END MY CODE###

# 🚨 Don't change the code below 👇
print(student_grade)

###InstructorCode###
for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"
    
print(student_grades)