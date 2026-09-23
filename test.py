import unittest

from main import gcd_recursive
from main import lcm


class TestGCD(unittest.TestCase):
    def test_recursive(self):
        self.assertEqual(gcd_recursive(48, 18), 6)
        self.assertEqual(gcd_recursive(48, 18), gcd_recursive(18, 48))
        self.assertEqual(gcd_recursive(0, 5), 5)
        self.assertEqual(gcd_recursive(-48, 18), 6)
        self.assertEqual(gcd_recursive(48, -18), 6)
        self.assertEqual(gcd_recursive(-48, -18), 6)
        self.assertEqual(gcd_recursive(1, 1), 1)
        self.assertEqual(gcd_recursive(0, 0), 0)

    def test_lcm(self):
        self.assertEqual(lcm(48, 18), 144)
        self.assertEqual(lcm(0, 5), 0)
        self.assertEqual(lcm(7, 0), 0)
        self.assertEqual(lcm(5, 7), 35)
        self.assertEqual(lcm(-48, 18), 144)
        self.assertEqual(lcm(0, 0), 0)

if __name__ == "__main__":
    unittest.main()