import unittest
from datetime import datetime as dt
import red_pencil as rp

one_row = [(dt(1, 1, 1), 1.12)]
two_rows = [(dt(1, 1, 1), 10.00), (dt(2, 1, 1), 8.00)]
three_rows = [(dt(1, 1, 1), 10.00), (dt(2, 1, 1), 8.00), (dt(2, 1, 28), 6.00),] # not 30 for last
three_rows_return_two = [(dt(1, 1, 1), 10.00), (dt(2, 1, 1), 8.00), (dt(2, 2, 28), 6.00),]

class TestIsRedPencil(unittest.TestCase):
    def test_when_is_red_pencil_passed_arrays_return_none(self):
        self.assertIsNone(rp.is_red_pencil([dt(1, 1, 1), 1.00], [dt(1, 1, 1), 1.00]))

    def test_when_is_red_pencil_passed_greater_second_price_return_false(self):
        self.assertFalse(rp.is_red_pencil((dt(1, 1, 1), 1.00), (dt(1, 2, 1), 2.00)))

    def test_when_is_red_pencil_passed_4_percent_reduction_return_false(self):
        self.assertFalse(rp.is_red_pencil((dt(1, 1, 1), 1.00), (dt(1, 2, 1), .96)))

    def test_when_is_red_pencil_passed_31_percent_reduction_return_false(self):
        self.assertFalse(rp.is_red_pencil((dt(1, 1, 1), 1.00), (dt(1, 2, 1), .69)))

    def test_when_is_red_pencil_passed_5_percent_reduction_return_true(self):
        self.assertTrue(rp.is_red_pencil((dt(1, 1, 1), 1.00), (dt(1, 2, 1), .95)))

    def test_when_is_red_pencil_passed_29_days_after_price_change_return_false(self):
        self.assertFalse(rp.is_red_pencil((dt(1, 1, 1), 1.00), (dt(1, 1, 30), .95)))

    def test_when_is_red_pencil_passed_29_after_red_pencil_return_false(self):
        self.assertFalse(rp.is_red_pencil((dt(1, 1, 1), 1.00), (dt(1, 2, 1), .95), dt(1, 1, 3)))

class TestShouldRedPencilEnd(unittest.TestCase):
    def test_when_should_red_pencil_end_passed_new_greater_return_true(self):
        self.assertTrue(rp.should_red_pencil_end((dt(1, 1, 1), 1.00), (dt(1, 2, 1), 1.01), 0))

    def test_when_should_red_pencil_end_passed_more_than_30_percent_original_return_true(self):
        self.assertTrue(rp.should_red_pencil_end((dt(1, 1, 1), 1.31), (dt(1, 2, 1), 1.31), 1.00))

class TestRedPencil(unittest.TestCase):
    def test_when_is_red_pencil_passed_tuple_return_none(self):
        self.assertIsNone(rp.red_pencil(()))

    def test_when_red_pencil_passed_one_row_return_empty_array(self):
        self.assertEqual(rp.red_pencil(one_row), [])

    def test_when_red_pencil_passed_two_rows_return_1_red_pencil(self):
        self.assertEqual(rp.red_pencil(two_rows), [(dt(2, 1, 1), 8.00)])

    def test_when_red_pencil_passed_three_rows_return_1_red_pencil(self):
        self.assertEqual(rp.red_pencil(three_rows), [(dt(2, 1, 1), 8.00)])

    def test_when_red_pencil_passed_three_rows_return_2_red_pencil(self):
        self.assertEqual(rp.red_pencil(three_rows_return_two), [(
            dt(2, 1, 1), 8.00), (dt(2, 2, 28), 6.00)])
