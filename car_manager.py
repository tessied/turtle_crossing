from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0.5


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        car = Turtle(shape="square")
        car.pu()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.setheading(180)
        car.goto(300, random.randint(-240, 240))
        car.color(random.choice(COLORS))
        self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
            if car.xcor() < -300:
                car.hideturtle()
                self.all_cars.remove(car)

    def hit_turtle(self, turtle):
        for car in self.all_cars:
            if car.distance(turtle) < 21:
                return True
        return False

    def speed_up(self):
        for car in self.all_cars:
            self.car_speed += MOVE_INCREMENT
