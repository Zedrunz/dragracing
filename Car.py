import arcade

class Car:
    def __init__(self):
        self.sprites = arcade.SpriteList()

        self.body = arcade.Sprite("resources/cars/car.png", scale=0.3)
        self.front_wheel = arcade.Sprite("resources/rims/wheel.png", scale=0.25)
        self.rear_wheel = arcade.Sprite("resources/rims/wheel.png", scale=0.25)

        self.sprites.append(self.body)
        self.sprites.append(self.front_wheel)
        self.sprites.append(self.rear_wheel)

        self.body.position = (200, 450)
        self.front_wheel.position = (259, 425)
        self.rear_wheel.position = (141, 425)

        self.speed = 0

    def update(self):
        self.body.center_x += self.speed
        self.front_wheel.center_x += self.speed
        self.rear_wheel.center_x += self.speed

        self.front_wheel.angle += self.speed
        self.rear_wheel.angle += self.speed

    def draw(self):
        self.sprites.draw()