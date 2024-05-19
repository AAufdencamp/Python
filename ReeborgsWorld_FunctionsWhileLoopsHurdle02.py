#####ReebordWorld-Hurdle02-WhileLoopPractice###

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
  
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

##Hurdle_01 has a fixed number of hurdles, so in terms of while loops##
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -=1
    print(number_of_hurdles)

###Hurdle_2#### 
###in Hurdle 2 the goal flag (and therefore hurdles to jump) is randomized

hurdle = 0
while at_goal() == False:
    jump()
    hurdle +=1
    print(hurdle)