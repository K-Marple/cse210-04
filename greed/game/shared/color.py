class Color:
    """A color.
    
    The responsibility of Color is to hold and provide information about itself. Color has a few
    convenience methods for comparing them and converting to a tuple.
    
    Attributes:
        _red (int): the red value.
        _green (int): the green value.
        _blue (int): the blue value.
        _alpha (int): the alpha or opacity.
    """

    def __init__(self, red, green, blue, alpha = 255):
        """Constructs a new Color using the specified red, green, blue and alpha values. The alpha
        value is the color's opacity.
        
        Args:
            red (int): a red value.
            green (int): a green value.
            blue (int): a blue value.
            alpha (int): an alpha or opacity.
        """
        self._red = red
        self._green = green
        self._blue = blue
        self._alpha = alpha

    def to_tuple(self):
        """Gets the color as a tuple of four values (red, green, blue, alpha).
        
        Returns:
            Tuple (int, int, int, int): the color as a tuple.
        """
        return (self._red, self._green, self._blue, self._alpha)