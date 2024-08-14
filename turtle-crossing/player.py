#Create a turtle player that starts at the bottom of the screen and listen
# for the "Up" keypress to move the turtle north.
from turtle import Turtle


STARTING_POSITION = (0, -280) #tuple
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):  #he player class is going to be the turtle which we're controlling to cross the road
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
