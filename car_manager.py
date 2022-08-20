from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.penup()
        self.hideturtle()
        self.number = 0
        self.y_value = 0
        self.move_speed = 5

    def make_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car_y = random.randint(-250, 250)
            new_car.goto(300, new_car_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_speed)

    def level_up(self):
        self.move_speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT



