import unittest

from main import gcd_recursive
from main import lcm
from main import find_gcd_slow
from main import gcd_iterative_fast


class TestGCD(unittest.TestCase):
    def test_recursive(self):
        self.assertEqual(gcd_recursive(1071, 462), 21)
        self.assertEqual(gcd_recursive(1071, 462), gcd_recursive(462, 1071))
        self.assertEqual(gcd_recursive(0, 13), 13)
        self.assertEqual(gcd_recursive(-1071, 462), 21)
        self.assertEqual(gcd_recursive(1071, -462), 21)
        self.assertEqual(gcd_recursive(-1071, -462), 21)
        self.assertEqual(gcd_recursive(17, 17), 17)
        self.assertEqual(gcd_recursive(0, 0), 0)

    def test_lcm(self):
        self.assertEqual(lcm(1071, 462), 23562)
        self.assertEqual(lcm(0, 13), 0)
        self.assertEqual(lcm(11, 0), 0)
        self.assertEqual(lcm(11, 13), 143)
        self.assertEqual(lcm(-1071, 462), 23562)
        self.assertEqual(lcm(0, 0), 0)

    def test_gcd_slow(self):
        self.assertEqual(find_gcd_slow(48, 18), 6)
        self.assertEqual(find_gcd_slow(18, 48), 6)
        self.assertEqual(find_gcd_slow(0, 5), 5)
        self.assertEqual(find_gcd_slow(5, 0), 5)
        self.assertEqual(find_gcd_slow(-48, 18), 6)
        self.assertEqual(find_gcd_slow(48, -18), 6)
        self.assertEqual(find_gcd_slow(-48, -18), 6)
        self.assertEqual(find_gcd_slow(1, 1), 1)
        self.assertEqual(find_gcd_slow(0, 0), 0)

    def test_gcd_fast(self):
        self.assertEqual(gcd_iterative_fast(2, 4), 2)
        self.assertEqual(gcd_iterative_fast(24, 60), 12)
        self.assertEqual(gcd_iterative_fast(36, 48), 12)
        self.assertEqual(gcd_iterative_fast(432, 111), 3)
        self.assertEqual(gcd_iterative_fast(1118, 2064), 86)

if __name__ == "__main__":
    unittest.main()
    