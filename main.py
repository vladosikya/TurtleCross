import turtle, player, cars, scoreboard, collision
import time

screen = turtle.Screen()
screen.tracer(0)
screen.listen()
screen.colormode(255)

car = cars.Cars()
player_turtle = player.Player()
level = scoreboard.ScoreBoard()
collisions = collision.Collision(car, player_turtle, level)
GAME = True

while collisions.GAME:
    screen.onkeypress(player_turtle.move_up, "Up")
    screen.onkeypress(player_turtle.move_down, 'Down')
    car.move()
    collisions.collision_next_level()
    collisions.collision_cars()
    if collisions.GAME == False:
        level.loose()

    time.sleep(0.1)
    screen.update()


screen.exitonclick()