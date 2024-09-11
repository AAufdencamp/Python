#create screen w 800 x h 600, black background, exit upon click
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0) #0 turns off animation. We want the paddle to appear instantanesouly on the RHS.
#when .tracer(0) is set to zero you have to manually update the screen and refresh it every single time.
#using screen.update(). To do this you need a while loop to check for a programming "switch" variable
#in this game our "switch" variable is game_is_on = True. See below code

r_paddle = Paddle((350,0)) #tuple for paddle location
l_paddle = Paddle((-350,0)) #tuple for paddle location


ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True #our program switch variable:-)

while game_is_on:
    time.sleep(ball.move_speed) #slows down the ball movement via slowing down the while loop in between updates using time module
    screen.update() #all code above has happend "in the background" at the time of calling this update. We
                    #will see the paddle(s) appear instantaneously on the RHS

    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    #Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        print(ball.move_speed)


    # Detect R paddle missed
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle missed
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()