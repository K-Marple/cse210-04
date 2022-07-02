from game.cast.player import Player


class Mineral(Player):
    """A naturally occuring homogeneous solid.
    
    The responsibility of a Mineral is to provide a instance of itself.
    
    Attributes:
        _type (string): the type of mineral (rock or gem).
    """

    def __init__(self):
        super().__init__()
        self._type = ""

    def get_type(self):
        """Gets the mineral's type.
        
        Returns:
            string: the type.
        """
        return self._type

    def set_type(self, type):
        """Updates the type to the given one.
        
        Args:
            type (string): the given type.
        """
        self._type = type