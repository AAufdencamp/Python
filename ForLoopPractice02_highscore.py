####ForLoop02_HighScore_MyCode####

# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
#goal to use for loop; avoid max()

score = 0

for i in student_scores:
  if score < i:
    score = i
    if score >= i:
      score = i
print(f"The highest score in the class is: {score}")    

###########InstructorCode###########
# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Your code below this row 👇
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
    # print(highest_score)

print(f"The highest score in the class is: {highest_score}")