class Collision:
    def __init__(self, cars, player, score):
        self.cars = cars
        self.player = player
        self.score = score
        self.GAME = True

    def collision_next_level(self):
        if self.player.ycor() >= 250:
            self.score.score+=1
            self.score.reset_level()
            self.cars.next_level()
            self.player.goto(0, -250)
            self.cars.random_positions()

    def collision_cars(self):
        for car in self.cars.cars:
            if self.player.distance(car) <= 25:
                self.GAME = False
            elif self.player.distance(car) <= 30 and car.ycor() - 10 <= self.player.ycor() <= car.ycor() + 10:
                self.GAME = False