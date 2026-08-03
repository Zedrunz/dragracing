import arcade
from pyglet.event import EVENT_HANDLE_STATE

from Car import Car
from carparts.Engines import Engines
from levels.menu import LVL

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Drag Game"

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.button_start_pressed = False
        self.ride = LVL(False)
    def setup(self):
        if self.ride.key is True:
            arcade.set_background_color(arcade.color.BLACK)

            self.camera = arcade.Camera2D()

            self.car = Car()
            #self.engine = engines.engineI4()

            self.accelerate = False
            self.rear = False

            self.accelerate_speed = 0.5

        else:
            arcade.set_background_color(arcade.color.BLACK)



    def on_draw(self):
        self.clear()

        if self.ride.key is True:
            self.camera.use()
            arcade.draw_line(
                0, 400,
                50000, 400,
                arcade.color.GRAY,
                line_width=20
            )

            self.car.draw()

            arcade.draw_text(
                f"Speed: {self.car.speed:.0f}",
                self.car.body.center_x - 100,
                self.car.body.center_y + 120,
                arcade.color.WHITE,
                20
            )
        else:
            self.clear()
            arcade.draw_lbwh_rectangle_filled(200, 800, 1000, 250, arcade.color.WHITE)


    def on_update(self, delta_time):
        if self.ride.key is True:
            if self.accelerate:
                self.car.speed += self.accelerate_speed

            if self.rear:
                self.car.speed -= self.accelerate_speed

            if not self.accelerate and self.car.speed > 0:
                self.car.speed -= 0.2

            if self.car.speed < 0:
                self.car.speed = 0

            self.car.update()

            self.camera.position = (
                self.car.body.center_x,
                self.car.body.center_y
            )
        else:
            if self.button_start_pressed:
                self.ride.key = True
                self.setup()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> EVENT_HANDLE_STATE:
        if 200 < x < 1200 and 800 < y < 1050:
            self.button_start_pressed = True

    def on_key_press(self, symbol, modifiers):
        if self.ride.key is True:
            if symbol == arcade.key.W:
                self.accelerate = True

            if symbol == arcade.key.S:
                self.rear = True

    def on_key_release(self, symbol, modifiers):
        if self.ride.key is True:
            if symbol == arcade.key.W:
                self.accelerate = False

            if symbol == arcade.key.S:
                self.rear = False


def main():
    game = MyGame()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()