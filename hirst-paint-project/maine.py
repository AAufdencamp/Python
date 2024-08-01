
###Code Challenge: use colorgram.py 1.2.0 to extract colors into a list of tuples from user choice
###of Hirst spot painint####

###My Code###
#https://pypi.org/project/colorgram.py/
# from colorgram import Color
# import colorgram

# colors = colorgram.extract('image.jpg', 10)
#
# color_list = []
# for i in colors:
#     color_list.append(i.rgb)
# print(color_list)
#
# print(color_list[0].r)
#
# color_values = []
# for i in color_list:
#     red = i.r
#     green = i.g
#     blue = i.b
#     color_values.append((red, green, blue)) #tuples
# print(color_values)
###End My Cod###

###Instructor Code###
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)
###End Instructor Code###

#copied from console into main.py
# check tuples in RGB calculator and remove any white. Encase tuple in rgb()
#https://www.w3schools.com/colors/colors_rgb.asp
# rgb_colors = [(252, 252, 252), (238, 248, 243), (251, 242, 246), (226, 237, 246), (30, 106, 145),
#               (229, 153, 80), (15, 169, 207), (148, 79, 30), (6, 57, 97), (31, 134, 77),
#               (214, 133, 162), (138, 32, 51), (205, 156, 22), (118, 172, 194), (213, 93, 124),
#               (235, 211, 85), (6, 103, 66), (145, 185, 167), (216, 209, 11), (3, 69, 136),
#               (15, 49, 43), (76, 83, 23), (243, 168, 151), (134, 59, 83), (53, 60, 15), (223, 170, 191),
#               (230, 100, 40), (1, 90, 120), (71, 157, 105), (164, 29, 25)]

color_list = [(238, 248, 243), (251, 242, 246), (226, 237, 246), (30, 106, 145),
              (229, 153, 80), (15, 169, 207), (148, 79, 30), (6, 57, 97), (31, 134, 77),
              (214, 133, 162), (138, 32, 51), (205, 156, 22), (118, 172, 194), (213, 93, 124),
              (235, 211, 85), (6, 103, 66), (145, 185, 167), (216, 209, 11), (3, 69, 136),
              (15, 49, 43), (76, 83, 23), (243, 168, 151), (134, 59, 83), (53, 60, 15), (223, 170, 191),
              (230, 100, 40), (1, 90, 120), (71, 157, 105), (164, 29, 25)]

#use Turtle and color_list to paint 10 x 10 grid of dots of size 20, spacing apart by 50 paces
#https://docs.python.org/3/library/turtle.html

from turtle import Turtle, Screen
import turtle
import random


tim = Turtle()

screen = Screen()
screen.colormode(255)
tim.ht()
#tim.pencolor(random.choice(color_list))
#tim.forward(50)
choice = random.choice(color_list)
# for i in range(100):
#     steps = int(random.random() * 100)
#     angle = int(random.random() * 360)
#     choice = random.choice(color_list)
#     tim.pencolor(choice)
#     tim.right(angle)
#     tim.fd(steps)

turtle.mode("logo")
print(turtle.window_width()) #960
print(turtle.window_height()) #810
              #N, E, S, W
logo_mode = [0, 90, 180, 270]

                #E,N,W,S
#standard_mode = [0, 90, 180, 270]
print(tim.pos())
tim.dot(20, choice)
tim.seth(0)
tim.penup()
tim.speed("slow")
steps = 50
initial_p = -250

def grid():
    initial_p = -250

    for i in range(0,10):
        tim.setposition(initial_p, 0)
        tim.seth(0)
        for i in range(0,5):
            tim.dot(20, random.choice(color_list))
            tim.fd(50)
        tim.setposition(initial_p,0)
        tim.seth(180)
        for i in range(0,6):
            tim.dot(20, random.choice(color_list))
            tim.fd(50)
        initial_p += 50




grid()

screen.exitonclick()

####END MY CODE:-)#####

