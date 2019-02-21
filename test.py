class Foo:
    """
    This is the Foo class.

    Create powerful Foo objects for generating foobars

    Example:
            >>> from test import Foo
            >>> x = Foo(6)
            >>> x.bar()
            >>> bar
            >>> bar
            >>> bar
            >>> bar
            >>> bar
    Attributes:
        power (int): Amount of bar energy contained in this Foo instance.
    """
    def __init__(self, barPower):
        """Initialize Foo object.

        Args:
            barPower (int): The bar energy to be contained in this Foo instance.
        Raises:
            AssertError: if barPower is less than 6.
            
        """
        assert barPower>5, "bar is too weak"
        self.power = barPower
    
    def bar(self):
        """Generate foobars based on bar energy."""
        for x in range(0,self.power):
            print('foobar')
