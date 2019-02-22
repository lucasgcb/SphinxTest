from _errors import _ERR_NOTLIST, _ERR_NOT3D

class Waldo:
    """This is the Waldo class
        
        Parameters
        ----------
        pos :  (Tuple(int,int,int)): 
            Waldo's current position
        
        Arguments
        ---------
        pos :  (Tuple(int,int,int)): 
            Start Waldo in this position

    """

    def __init__(self, pos):
        

        assert type(pos) == list, _ERR_NOTLIST
        assert len(pos) == 3, _ERR_NOT3D
        self.pos=pos

    def whereIsHe(self):
        """Show Waldo's Position
        
        Returns
        -------
        list:
            3 dimension coordinate of Waldo's position
            
        Example
        -------
        >>> Waldo([2,3,5])
        >>> Waldo.whereIsHe()
        >>> [2,3,5]
        """

        print(self.pos)
    