from game.shared.color import Color
from game.shared.point import Point


class Player:
    """A visible, moveable thing that participates in the game.
    
    The responsibility of Player is to keep track of its appearance, position and velocity in
    2D space.
    
    Attributes:
        _text (string): the text to display.
        _font_size (int): the font size to use.
        _color (Color): the color of the text.
        _position (Point): the screen coordinates.
        _velocity (Point): the speed and direction.
    """

    def __init__(self):
        """Constructs a new Player."""
        self._text = ""
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def get_color(self):
        """Gets the player's color as a tuple of three ints (r, g, b).
        
        Returns:
            color: the player's text color.
        """
        return self._color

    def get_font_size(self):
        """Gets the player's font size.
        
        Returns:
            point: the player's position in 2D space.
        """
        return self._font_size

    def get_position(self):
        """Gets the player's position in 2D space.
        
        Returns:
            point: the player's position in 2D space.
        """
        return self._position

    def get_text(self):
        """Gets the player's textual representation.
        
        Returns:
            string: the player's textual representation.
        """
        return self._text

    def get_velocity(self):
        """Gets the player's speed and direction.
        
        Returns:
            point: the player's speed and direction.
        """
        return self._velocity

    def move_next(self, max_x, max_y):
        """Moves the player to its next position according to its velocity. Will wrap the position
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): the maximum x value.
            max_y (int): the maximum y value.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)

    def set_color(self, color):
        """Updates the color to the given one.
        
        Args:
            color (Color): the given color.
        """
        self._color = color

    def set_position(self, position):
        """Updates the position to the given one.
        
        Args:
            position (Point): the given position.
        """
        self._position = position

    def set_font_size(self, font_size):
        """Updates the font size to the given one.
        
        Args:
            font_size (int): the given font size.
        """
        self._font_size = font_size

    def set_text(self, text):
        """Updates the text to the given value.
        
        Args:
            text (string): the given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Point): the given velocity.
        """
        self._velocity = velocity