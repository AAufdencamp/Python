#Create cars that are 20px high by 40px wide that are randomly generated
# along the y-axis and move to the left edge of the screen.
# No cars should be generated in the top and bottom 50px of the screen
# (think of it as a safe zone for our little turtle).
# Hint: generate a new car only every 6th time the game loop runs.
# If you get stuck, check the video walkthrough in Step 4.
from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle): #the car manager is going to generate all of the random cars and move them across the screen,
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            #create 1/6 change of creating new car will slow down production of cars and give turtle a chance!
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len= 2) #stretch to scale. Original D: 20x20. Widthx2 and Lengthx1
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-250, 250) #gives turtle start-/finish-line buffer
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        #loop through list of all cars and for each car move backward 5 paces
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)


    def level_up(self):
        self.car_speed += MOVE_INCREMENT




# Detect when the turtle player collides with a car and stop the game if this happens.
# If you get stuck, check the video walkthrough in Step 5.

#Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y).
# When this happens, return the turtle to the starting position and increase the speed of the cars.
# Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed.
# If you get stuck, check the video walkthrough in Step 6.