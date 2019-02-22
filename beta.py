from _errors import _ERR_NOTLIST, _ERR_NOT3D

class Waldo:
    """This is the Waldo Docstring

        Example:
            >>> Waldo([2,3,5])
            >>> Waldo.whereIsHe()
            >>> [2,3,5]
    """

    def __init__(self, pos):
        """Init Waldo.
        
        Args:
            pos (Tuple(int,int,int)): Initialize Waldo in this position 
        """

        assert type(pos) == list, _ERR_NOTLIST
        assert len(pos) == 3, _ERR_NOT3D
        self.pos=pos

    def whereIsHe(self):
        """Show Waldo's Position"""

        print(self.pos)
    