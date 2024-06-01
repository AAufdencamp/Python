#Paint Area Calculator#
# Define a function called paint_calc() so the code below works. 

# My code below this line 👇
import math
def paint_calc(height, width , cover):
    print(f"You'll need {int(math.ceil((height * width) / cover))} cans of paint.") 
# My code above this line 👆
  

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

###***InstructorCode***###
#import math

#def paint_calc(height, width, cover):
  #num_cans = (height * width) / cover
  #round_up_cans = math.ceil(num_cans)
  #print(f"You'll need {round_up_cans} cans of paint.")

###***EndInstructorCode***###