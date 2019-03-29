import unittest
from datetime import datetime as dt
import red_pencil as rp

one_row = [(dt(1, 1, 1), 1.12)]
two_rows = [(dt(1, 1, 1), 10.00), (dt(2, 1, 1), 8.00)]
two_rows_not_promo_range = [
    (dt(1, 1, 1), 10.00),
    (dt(2, 1, 1), 5.00)
]
three_rows = [ # not 30 days for last
    (dt(1, 1, 1), 10.00),
    (dt(2, 1, 1), 8.00),
    (dt(2, 1, 28), 7.90),
]
three_rows_return_two = [
    (dt(1, 1, 1), 10.00),
    (dt(2, 1, 2), 8.00),
    (dt(2, 2, 28), 6.00),
]
# returns 0 because price not stable for 30 days on last one
three_rows_return_none = [
    (dt(1, 1, 1), 10.00),
    (dt(1, 1, 2), 9.00),
    (dt(1, 1, 3), 8.10),
]
# return two because price immediately ended promotion
three_rows_end_early = [
    (dt(1, 1, 1), 10.00),
    (dt(1, 2, 2), 8.00),
    (dt(1, 2, 3), 8.10),
]
# check not prolonged by further price decrease
three_rows_price_decrease = [
    (dt(1, 1, 1), 10.00),
    (dt(1, 2, 2), 8.00),
    (dt(1, 2, 28), 7.50),
]
# check price reduced more than 30% original
three_rows_30_percent = [
    (dt(1, 1, 1), 10.00),
    (dt(1, 2, 2), 8.00),
    (dt(1, 2, 4), 6.50),
]

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

    def test_when_should_red_pencil_end_passed_less_than_30_percent_original_return_true(self):
        self.assertTrue(rp.should_red_pencil_end((dt(1, 1, 1), 1.31), (dt(1, 2, 1), 1.31), 2.00))

class TestRedPencil(unittest.TestCase):
    def test_when_is_red_pencil_passed_tuple_return_none(self):
        self.assertIsNone(rp.red_pencil(()))

    def test_when_red_pencil_passed_one_row_return_empty_array(self):
        self.assertEqual(rp.red_pencil(one_row), ([], []))

    def test_when_red_pencil_passed_two_rows_return_1_red_pencil(self):
        self.assertEqual(rp.red_pencil(two_rows), (
            [(dt(2, 1, 1), 8.00)], # red pencil start
            [dt(2, 1, 31)] # red pencil end
        ))

    def test_when_red_pencil_passed_three_rows_return_1_red_pencil(self):
        self.assertEqual(rp.red_pencil(three_rows), (
            [(dt(2, 1, 1), 8.00)],
            [dt(2, 1, 31)]
        ))

    def test_when_red_pencil_passed_three_rows_return_2_red_pencil(self):
        self.assertEqual(rp.red_pencil(three_rows_return_two), (
            [(dt(2, 1, 2), 8.00), (dt(2, 2, 28), 6.00)],
            [dt(2, 2, 1), dt(2, 3, 30)]
        ))

    def test_when_red_pencil_passed_three_rows_return_none(self):
        self.assertEqual(rp.red_pencil(three_rows_return_none), ([], []))

    def test_when_red_pencil_passed_three_rows_end_early_return_1(self):
        self.assertEqual(rp.red_pencil(three_rows_end_early), (
            [(dt(1, 2, 2), 8.00)],
            [dt(1, 2, 3)],
        ))

    def test_when_red_pencil_passed_two_rows_not_promo_range_return_none(self):
        self.assertEqual(rp.red_pencil(two_rows_not_promo_range), ([], []))

    def test_when_red_pencil_passed_three_rows_price_decrease_return_1(self):
        self.assertEqual(rp.red_pencil(three_rows_price_decrease), (
            [(dt(1, 2, 2), 8.00)],
            [dt(1, 3, 4)],
        ))

    def test_when_red_pencil_passed_three_rows_30_percent_return_1(self):
        self.assertEqual(rp.red_pencil(three_rows_30_percent), (
            [(dt(1, 2, 2), 8.00)],
            [dt(1, 2, 4)],
        ))
