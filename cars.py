from turtle import Turtle
import random

class Cars:
    def __init__(self):
        self.cars = []
        self.speed = 2
        for _ in range(30):
            car = Turtle(shape='square')
            car.shapesize(stretch_len=2)
            car.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            car.penup()
            self.cars.append(car)
        self.random_positions()

    def random_positions(self):
       for car in self.cars:
           car.goto(random.randint(-300, 300), random.randint(-200, 200))

    def move(self):
        for car in self.cars:
            if car.xcor() >= 350:
                car.goto(random.randint(-370, -350), random.randint(-200, 200))
            car.forward(self.speed)

    def next_level(self):
        self.speed+=4