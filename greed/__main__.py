from random import randint, choice

from game.cast.actor import Actor
from game.cast.mineral import Mineral
from game.cast.cast import Cast

from game.director.director import Director

from game.services.keyboard import Keyboard
from game.services.video import Video

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_MINERALS = 20


def main():

    # create the cast
    cast = Cast()

    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)

    # create the minerals
    score = 0
    for n in range(DEFAULT_MINERALS):
        n = ["*", "o"]
        text = choice(n)
        if text == "*":
            score += 1
        elif text == "o":
            score -= 1

        x = randint(1, COLS - 1)
        y = randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        color = Color(r, g, b)

        mineral = Mineral()
        mineral.set_text(text)
        mineral.set_font_size(FONT_SIZE)
        mineral.set_color(color)
        mineral.set_position(position)
        mineral.set_score(score)
        cast.add_actor("minerals", mineral)

    # start the game
    keyboard = Keyboard(CELL_SIZE)
    video = Video(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard, video)
    director.start_game(cast)

if __name__ == "__main__":
    main()