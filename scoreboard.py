import turtle

class ScoreBoard():
    def __init__(self):
        self.score = 0
        self.level = turtle.Turtle()
        self.level.hideturtle()
        self.reset_level()

    def reset_level(self):
        self.level.clear()
        self.level = turtle.Turtle()
        self.level.penup()
        self.level.hideturtle()
        self.level.goto(-250, 250)
        self.level.write(arg=f"Level {self.score}", align='center', font=('Arial', 25, 'bold'))

    def loose(self):
        self.level = turtle.Turtle()
        self.level.penup()
        self.level.hideturtle()
        self.level.goto(0, 0)
        self.level.write(arg=f"You're lose!", align='center', font=('Arial', 45, 'bold'))