# we're going to use inheritance to detect collision with food. Our snake should be able to hit a piece of food,
# which is just going to be a blue circle, and every time it touches the food, the circle moves to a new,
# random location on the screen.

from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(600, 600) #
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision w food
    if snake.head.distance(food) < 15: #15 pixels
        print("nom, nom, nom")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision w wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision w tail
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick() #leave as last line of code