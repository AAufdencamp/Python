####ReeborgsWorld--Hurdle#3-MyCode####

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
 
###Hurdle_3###
###both hurdle spacing and goal flag are randomized
##MyCode####

while front_is_clear() and at_goal() == False:
    move()
        
while at_goal() == False:
    if not front_is_clear():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
    if front_is_clear() and at_goal() == False:
        move()

###end-my-code####

##InstructorCode###        
    #while not at_goal():
        #if wall_in_front():
            #jump02()
        #else:
            #move()
#####EndInstrtuctorCode### 