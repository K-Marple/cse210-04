class Point:
    """A distance from a relative origin (0, 0).
    
    The responsibility of Point is to hold and provide information about itself. Point has a few
    convenience methods for adding, scaling, and comparing them.
    
    Attributes:
        _x (int): the horizontal distance from the origin.
        _y (int): the vertical distance from the origin.
    """

    def __init__(self, x, y):
        """Constructs a new Point using the specified x and y values.
        
        Args:
            x (int): the specified x value.
            y (int): the specified y value.
        """
        self._x = x
        self._y = y

    def add(self, other):
        """Gets a new point that is the sum of this and the given one.
        
        Args:
            other (Point): the point to add.
        
        Returns:
            Point: a new point that is the sum.
        """
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    def equals(self, other):
        """Whether or not this Point is equal to the given one.
        
        Args:
            other (Point): the point to compare.
            
        Returns:
            bool: True if both x and y are equal; False if otherwise.
        """
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        """Gets the horizontal distance.
        
        Returns:
            int: the horizontal distance.
        """
        return self._x

    def get_y(self):
        """Gets the vertical distance.
        
        Returns:
            int: the veritcal distance.
        """
        return self._y

    def scale(self, factor):
        """Scales the point by the provided factor.
        
        Args:
            factor (int): the amount to scale.
            
        Returns:
            Point: a new point that is scaled.
        """
        return Point(self._x * factor, self._y * factor)