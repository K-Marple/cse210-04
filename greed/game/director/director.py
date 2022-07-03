from random import randint, choice

from game.cast.mineral import Mineral
from game.shared.color import Color
from game.shared.point import Point

class Director:
    """A person who directs the game.
    
    The responsibility of a Director is to control the steps of the game.
    
    Attributes:
        _keyboard (Keyboard): for getting directional input.
        _video (Video): for providing video output.
    """

    def __init__(self, keyboard, video):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard (Keyboard): an instance of Keyboard.
            video (Video): an instance of video.
        """
        self._keyboard = keyboard
        self._video = video

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.
        
        Args:
            cast (Cast): the cast of actors.
        """
        self._video.open_window()
        while self._video.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
            
        Args:
            cast (Cast): the cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard.get_direction()
        robot.set_velocity(velocity)

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with minerals.
            
        Args:
            cast (Cast): the cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        minerals = cast.get_actors("minerals")
        score = cast.get_first_actor("scores")

        banner.set_text("")
        max_x = self._video.get_width()
        max_y = self._video.get_height()
        robot.move_next(max_x, max_y)

        score = banner.get_score()
        banner.set_score(score)
        banner.set_text(f"Score: {score}")

        for mineral in minerals:
            if robot.get_position().equals(mineral.get_position()):
                score = banner.get_score() + mineral.get_score()
                banner.set_score(score)
                banner.set_text(f"Score: {score}")

                cast.remove_actor("minerals", mineral)

                text = choice(["o", "*"])
                cols = (self._video.get_height() / self._video.get_cell_size())
                rows = (self._video.get_width() / self._video.get_cell_size())
                x = randint(1, cols - 1)
                y = randint(1, rows - 1)
                position = Point(x, y)
                cell_size = self._video.get_cell_size()
                position = position.scale(cell_size)

                r = randint(0, 255)
                g = randint(0, 255)
                b = randint(0, 255)
                color = Color(r, g, b)
        
                another_mineral = Mineral()
                
                if text == "o":
                    another_mineral.set_score(-1)
                elif text == "*":
                    another_mineral.set_score(1)
                another_mineral.set_text(text)
                another_mineral.set_font_size(self._video.get_cell_size())
                another_mineral.set_color(color)
                another_mineral.set_position(position)
                another_mineral.set_velocity(Point(0, 4))

                cast.add_actor("minerals", another_mineral)
            
            position = mineral.get_position()
            max_x = self._video.get_width()
            max_y = self._video.get_height()
            mineral.move_next(max_x, max_y)

    def _do_outputs(self, cast):
        """Draws the actors on the screen.
          
        Args:
            cast (Cast): the cast of actors.
        """
        self._video.clear_buffer()
        actors = cast.get_all_actors()
        self._video.draw_actors(actors)
        self._video.flush_buffer()