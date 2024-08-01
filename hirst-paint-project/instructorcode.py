import turtle as turtle_module
import random
turtle_module.colormode(255) #because we are using rgb values btwn 0 and 255 we have to change the
#turtle module color mode

tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(238, 248, 243), (251, 242, 246), (226, 237, 246), (30, 106, 145),
              (229, 153, 80), (15, 169, 207), (148, 79, 30), (6, 57, 97), (31, 134, 77),
              (214, 133, 162), (138, 32, 51), (205, 156, 22), (118, 172, 194), (213, 93, 124),
              (235, 211, 85), (6, 103, 66), (145, 185, 167), (216, 209, 11), (3, 69, 136),
              (15, 49, 43), (76, 83, 23), (243, 168, 151), (134, 59, 83), (53, 60, 15), (223, 170, 191),
              (230, 100, 40), (1, 90, 120), (71, 157, 105), (164, 29, 25)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list)) #tap into random module and get hold of choice method
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen() #So let's create a new screen object from the turtle module and
# the class is called Screen. Then we can get our screen to change its behavior by calling exitonclick.

screen.exitonclick() #only when we click on it does the screen disappear

