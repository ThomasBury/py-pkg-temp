"""
Dumming module for illustrating special methods

"""

class Fibonacci:
    """Create a Fibonacci class for computing the elements of the sequence
    
    Parameters
    ----------
        n : int
            the nth sequence element

        
    Attributes
    ----------
    cache : List[int]
        cache for computing faster
    """
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # This method turns the instances of Fibonacci into callable objects
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]