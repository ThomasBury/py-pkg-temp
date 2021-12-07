"""
A dummy module
"""

def hello_world(prt: bool = False):
    """Print some fancy text
    """
    fancy_text = "Quantum fluctuations"
    if prt:
        print(fancy_text)
    
    return fancy_text