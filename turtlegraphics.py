from turtle import Turtle, Screen
import turtle
import random

# # Turtle colors https://cs111.wellesley.edu/reference/colors
# # Turtle colors https://trinket.io/docs/colors
# #Turtle graphics documentation https://docs.python.org/3/library/turtle.html
# #use stackoverflow via Google with search terms including keyword Stackoverflow
#
tim = Turtle()
tim.shape("turtle")
tim.color("dark green")
# #https://www.tcl.tk/man/tcl/TkCmd/colors.htm
# #Turtle uses tkinter under the hood for graphics. See above links for visual rep of colors
# #we can us Python to create a Graphical User Interface
#

for i in range(4):
    tim.forward(100)
    tim.right(90)


print(tim.pos())
tim.shapesize(2,2,6)
tim.pensize(2.5)
tim.speed(1)
for _ in range(25):
    tim.color("lime")
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()
print(tim.pos())

######## Challenge 1 - Draw Shapes ############
#triangle 3 sides; external angles 120
tim.forward(100)
tim.right(120)
tim.forward(100)
tim.right(120)
tim.forward(100)
tim.right(120)

#square 4 sides; external angles 90
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)

#####My Code######
shapes = [
    {"sides": 3, "external_angle": 120},
    {"sides": 4, "external_angle":90},
    {"sides": 5, "external_angle":72},
    {"sides": 6, "external_angle":60},
    {"sides": 7, "external_angle":51.4},
    {"sides": 8, "external_angle":45},
    {"sides": 9, "external_angle":40},
    {"sides": 10, "external_angle":36},
]

i = 0
j= 0
color = ["yellow", "green yellow", "magenta", "violet", "orange red",
         "medium sea green", "light coral", "lime green"]

for index in range(len(shapes)):
    if i <= 7:
        for key in shapes[i]:
            n = shapes[i]["sides"]
            print(n)
            for j in range(n):
                tim.pencolor(random.choice(color))
                tim.forward(100)
                tim.right(shapes[i]["external_angle"])
                print(shapes[i]["external_angle"])
            i += 1

#####End My CODE############

####Instructor Code####

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat",
         "SlateGray", "SeaGreen"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)


####End Insturcotr Code###

#challenge 04 <- Random Walk https://en.wikipedia.org/wiki/Random_walk

##MY code challenge 04###
###tim.mode("logo") #initial heading up/north and positive angles clockwise
tim.seth(0) #to_angle 0 - north, 90 - east, 180 - south, 270 - west
directions = [0, 90, 180, 270] #logo

for steps in range(100):
    tim.pensize(10)
    go = random.choice(directions)
    tim.seth(go)
    tim.color(random.choice(colors))
    tim.forward(50)
########End My Code Challenge 04#######

##Instructor code challenge 04###
# turtle.colormode(255) #tap into turtle module directly to change RGB colormode to 255 scale
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fast")
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     #tim.pencolor(r,g,b) my solution
#     random_color = (r,g,b) #instructor sol
#     return random_color #instructor sol
#
#
# for _ in range(200):
#     #random_color() my solution
#     tim.color(random_color()) #insturtor sol
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

##End Instructor code challenge 04###

##Named Colors vs Random Colors
#tuple is a Python datatype, e.g. (1,3,8)
#elements in a tuple are ordered
#tuples are fixed, e.g, cannot be changed
#tuples are immutable
#EXCEPT: tuples can be converted into a list
# my_tuple = (1,3,8)
# list(my_tuple)

#https://www.w3schools.com/colors/colors_rgb.asp
#red, green and blue can be mixed to create any desired color

######Challenge 5###############

tim.speed("fastest")
tim.pensize(1)
tim.hideturtle()

for i in range(0,51):
    tim.pencolor(random.choice(colors))
    tim.circle(50)
    tim.left(10)
    print(i)
    #tim.fd(tim.tiltangle())


###Instructor Code###
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b) #instructor sol
    return color

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


#keep these two line of code at bottom to execute last
screen = Screen()
screen.screensize(800,600)
screen.exitonclick()

##################
#Importing Modules
# simple import -> keyword + modulename
# import reduced later work -> keyword + modulename + keyword + thing-in-module
# import everything -> keyword + modulename + *
# Examples:
# import turtle
# from turtle import Turtle (preferred code)
# from turtle import * (considered bad code)

#how to alias modules -> ie, import the module under a name we define.
# Example:
# import turtle as t
# tim = t.Turtle()

#installing modules not packaged into Python Standard library
#.venv is local virtual environment library. This is where package installs get stored
#virtual environment and installed modules get installed locally w/in your project.

