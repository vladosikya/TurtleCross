from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape('turtle')
        self.color('green')
        self.goto(0, -250)

    def move_up(self):
        self.forward(5)

    def move_down(self):
        if self.ycor() <= -250:
            pass
        else:
            self.back(5)
