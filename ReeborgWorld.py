###ReeborWorld--mycode--SquarePath
##https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

##practicing making functions##
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
turn_left()

move()

turn_right()

move()

turn_right()

move()

turn_right()

move()

turn_around()

#######EndPracticeMakingFunctions#########

####ReeborgHurdlesLoopChallenge######
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

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

for i in range(1, 6):
    jump()
    
move()
turn_left()
move()
turn_right()
move()
turn_right()
move()
 