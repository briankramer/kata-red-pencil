import unittest
from datetime import datetime as dt
import red_pencil as rp

class TestRedPencil(unittest.TestCase):
    def test_when_is_red_pencil_passed_arrays_return_none(self):
        self.assertIsNone(rp.is_red_pencil([dt(1, 1, 1), 1.00], [dt(1, 1, 1), 1.00]))
