from SphinxTest._errors import _ERR_LOWBAR

class Foo:
    """This is the Foo class.

    Create powerful Foo objects for generating foobars

    Attributes
    ----------
    power (int): 
        Amount of bar energy contained in this Foo instance.

    Parameters
    ----------
    barPower : int
        The bar energy to be contained in this Foo instance.
    
    Raises
    ------
    AssertError 
        If barPower is less than 6, crap itself.
            
    Examples
    --------

    >>> from test import Foo
    >>> x = Foo(6)
    >>> x.bar()
    >>> foobar0
    >>> foobar1
    >>> foobar2
    >>> foobar3
    >>> foobar4
    >>> foobar5
            
    """
    def __init__(self, barPower):



        
        assert barPower>5, _ERR_LOWBAR
        self.power = barPower
    
    def bar(self):
        """Generate foobars based on bar energy."""
        for x in range(0,self.power):
            print('foobar' + str(x))
