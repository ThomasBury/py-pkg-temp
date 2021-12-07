import pytest
import numpy as np
import pandas as pd
from pkgtemp.sub_pkg1.modB import hello_world


class TestHelloWorld:
    """
    Test suite for modB
    """

    def test_hello_world(self):
        # not task dependent (same for clf and regr)
        txt_out = hello_world()
        assert isinstance(txt_out, str), "the output should be a string"
