import unittest
import logging

from comparative import compare_by

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Clock:

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hour = hours
        self.minute = minutes
        self.second = seconds

    def __repr__(self):
        return ("Clock(h={0.hour:}, m={0.minute:02d}, "
                "s={0.second:02d})").format(self)

    def __str__(self):
        return "{0.hour:02d}:{0.minute:02d}:{0.second:02d}".format(self)


@compare_by("hour", "minute", "second")
class ComparableClock(Clock):
    pass


class TestDecoratorSetup(unittest.TestCase):

    def setUp(self):
        self.unwrapped = Clock(8,0)
        self.wrapped = ComparableClock(8,1)

    def test_decorator_returns_the_same_class(self):
        if type(self.unwrapped) != type(self.unwrapped):
            self.fail()

    def test_raises_type_error_if_no_comparison_attribute(self):
        with self.assertRaises(TypeError):
            _ = compare_by()(Clock)


class TestComparisons(unittest.TestCase):

    def setUp(self):
        self.clock1 = ComparableClock(8, 0, 0)
        self.clock2 = ComparableClock(8, 0, 1)
        self.clock3 = ComparableClock(8, 1, 0)
        self.clock1_dup = ComparableClock(8, 0, 0)

    def test_lt_returns_false_if_objs_are_equal(self):
        self.assertFalse(self.clock1 < self.clock1_dup)

    def test_lt_returns_false_if_obj1_gt_obj2(self):
        self.assertFalse(self.clock3 < self.clock2)
        self.assertFalse(self.clock2 < self.clock1)

    def test_lt_returns_true_if_obj1_lt_obj2(self):
        self.assertTrue(self.clock1 < self.clock2,
                "{} should be less than {}".format(self.clock1, self.clock2))

    def test_ne_returns_true_if_obj1_gt_obj2(self):
        self.assertNotEqual(self.clock2, self.clock1)

    def test_ne_returns_true_if_obj1_lt_obj2(self):
        self.assertNotEqual(self.clock1, self.clock2)

    def test_ne_returns_false_if_clocks_are_equal(self):
        self.assertFalse(self.clock1 != self.clock1_dup)

    def test_eq_returns_true_if_clocks_are_equal(self):
        self.assertEqual(self.clock1, self.clock1_dup,
                msg="equal clocks did not compare as equal")

    def test_eq_returns_false_if_clocks_are_not_equal(self):
        self.assertNotEqual(self.clock1, self.clock3)
        self.assertNotEqual(self.clock1, self.clock2)
        self.assertNotEqual(self.clock3, self.clock2)

    def test_le_returns_false_if_obj1_gt_obj2(self):
        self.assertFalse(self.clock3 <= self.clock2)


if __name__ == "__main__":
    unittest.main()