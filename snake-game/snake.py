from turtle import Screen, Turtle
import time

STARTING_POSITION = [(0,0), (-20,0), (-40,0)] #tuples. Var name represents a constant in all caps
MOVE_DISTANCE = 20 #seting another constance in this class by naming in all caps
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

screen = Screen()
screen.listen()

#self.head refers throughout as segments[0] because that is the segment that leads the way for the
#rest to follow

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        #add new segment to the snake
        self.add_segment(self.segments[-1].position()) #get hold of last index in the list and add new segment
        #to its position

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1 ):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)






#up 90, right 0, down 270, left 180
#And it's the fact that the snake can't move back on itself.
#It can't go forwards and then go the opposite direction because that requires
#the head to change directions.
# And this is not allowed in the official snake game.
# So how can we code this into our game? Well,
# we have to figure out when the head is pointing towards down direction,
# then we shouldn't allow it to go up. And similarly, when it's pointing up,
# we shouldn't let it go down, when it's pointing right
# we shouldn't let it go left