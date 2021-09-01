import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
cars = CarManager()

screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True
count = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.move_car()
    if count % 6 == 0:
        cars.new_car()
    count += 1
