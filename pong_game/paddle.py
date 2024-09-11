from turtle import Turtle, Screen

class Paddle(Turtle):  #carry the following out whenver we create a new object of Paddle class
    def __init__(self, position):
        super().__init__()  #initialize Turtle as super clas from which Paddle can inherit
        self.shape("square")  # all turtles start off 20x20
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  # we do this to widen our square into a triangle
        self.penup()
        self.goto(position) #here we establish that the Paddle class initilizer takes an argument for a
        # tuple for the position of each Paddle object

#recall we tap into methods and attributes by using self keyword

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

