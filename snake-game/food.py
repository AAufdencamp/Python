from turtle import Turtle
import random

class Food(Turtle):  #Turtle is superclass from which Food class inherits
    def __init__(self):
        super().__init__()  #initialize everything that the superclass Turtle has into our Food class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid= 0.5) #default is 20x20pixels. We want 10x10pixel circle
        self.color("blue")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randint(-280, 280)  # our screen is 600x600pixels
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


# all the above will happen as soon as we create a new food object from the Food class.
# Remember, whenever you initialize a new object from the class, the init gets called
