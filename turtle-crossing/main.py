import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
counter = 0
INTERVAL_TIME = 0.1
# for i in range(6):
#     car_manager.create_cars()

while game_is_on:
    time.sleep(INTERVAL_TIME) #whatever it is that you put inside this while loop, it's going to be refreshed every 0.1 seconds.
    screen.update()

    car_manager.create_car() #every 0.1 seconds a new car is created IF random.randit() lands on 1. See car_manager.
    car_manager.move_cars()

    ##My Solution to Detect Collision##
    # for i in range(0, len(car_manager.all_cars)):
    #     if player.distance(car_manager.all_cars[i]) <= 20:
    #         print("Game Over")
    #         game_is_on = False

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    ##My Solution to Detect Successful Crossing and Speed up animation##
    # if player.ycor() > 280:
    #     player.goto(0, -280)
    #     INTERVAL_TIME *= 0.9
    #     print(INTERVAL_TIME)

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()