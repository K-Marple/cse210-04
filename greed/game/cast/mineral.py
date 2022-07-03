from game.cast.actor import Actor


class Mineral(Actor):
    """A naturally occuring homogeneous solid.
    
    The responsibility of a Mineral is to provide a instance of itself.
    
    Attributes:
        _score (int): the score of mineral (rock = -1, gem = +1).
    """

    def __init__(self):
        super().__init__()
        self._score = 0

    def get_score(self):
        """Gets the mineral's score.
        
        Returns:
            int: the score.
        """
        return self._score

    def set_score(self, score):
        """Updates the score to the given one.
        
        Args:
            score (int): the given score.
        """
        self._score = score