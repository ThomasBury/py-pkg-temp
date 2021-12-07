# from . import pkgtemp

# __all__ = ["pkgtemp"]

# # bound to upper level
# from pkgtemp import *

import os

HERE = os.path.abspath(os.path.dirname(__file__))

ABOUT = {}  # type: ignore
with open(os.path.join(HERE, '__version__.py')) as f:
    exec(f.read(), ABOUT)

__version__ = ABOUT['__version__']