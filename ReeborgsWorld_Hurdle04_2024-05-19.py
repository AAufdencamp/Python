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

def jump02():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()  
    
####Hurdle04####
##MyCode##

while not at_goal():
    if front_is_clear() and not at_goal():
        move()
    if front_is_clear() == False and wall_in_front() and wall_on_right():
        turn_left() 
    if wall_on_right() and front_is_clear():
        move()        
    if not wall_on_right():
        turn_right()
        move()
        turn_right()
        move()
     
####endMyCode####    
    
###Instructor_Code###
def jump03():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump03()
    else:
        move() 

###endInstructorCode###            