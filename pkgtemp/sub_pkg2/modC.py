"""
A small module for illustrating the builtin methods

**The module structure is the following:**

- The ``Complex`` main class to create complex number object

"""


import numpy as np
from typing import Union, Callable, Optional, Tuple, List

class Complex:
    """Create a complex number class
    
    Parameters
    ----------
        a : float
            the real part
        b : float
            the imaginary part

        
    Attributes
    ----------
        part_re : float
            the real part
        part_im : float
            the imaginary part
    """
    def __init__(self, a=0, b=0):
        self.part_re = a
        self.part_im = b

    def __str__(self):
        """Print out the complex number in a nice format

        Returns
        -------
        [type]
            [description]
        """
        im_sgn = "+" if self.part_im >= 0 else "-" 
        return print(f"{self.part_re} {im_sgn} {abs(self.part_im)}i")

    def mod(self):
        """[summary]

        Returns
        -------
        float
            the module of the complex number
        """
        return np.sqrt(self.part_re ** 2 + self.part_im ** 2)

    # The 'other' argument in the following methods corresponds to the object
    # of type Complex that we wish to compare to

    def __lt__(self, other):
        """Compare the module of the complex number
        Says it is "smaller" if the module is smaller
        (not rigourous though)

        Parameters
        ----------
        other : Callable
            the other instance of complex

        Returns
        -------
        bool
            if is smaller than the other complex instance
        """
        return self.mod() < other.mod()

    def __gt__(self, other):
        """Compare the module of the complex number
        Says it is "larger" if the module is larger
        (not rigourous though)

        Parameters
        ----------
        other : Callable
            the other instance of complex

        Returns
        -------
        bool
            if is larger than the other complex instance
        """
        return self.mod() > other.mod()
