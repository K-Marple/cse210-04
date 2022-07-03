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

        banner.set_text("")
        max_x = self._video.get_width()
        max_y = self._video.get_height()
        robot.move_next(max_x, max_y)

        for mineral in minerals:
            if robot.get_position().equals(mineral.get_position()):
                score = mineral.get_score()
                banner.set_text(f"Score: {score}")

    def _do_outputs(self, cast):
        """Draws the actors on the screen.
          
        Args:
            cast (Cast): the cast of actors.
        """
        self._video.clear_buffer()
        actors = cast.get_all_actors()
        self._video.draw_actors(actors)
        self._video.flush_buffer()