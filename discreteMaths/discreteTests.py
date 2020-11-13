import unittest
from . import elementary as el

class TestElementary(unittest.TestCase):

    def test_common_divisors(self):
        self.assertTrue(el.commonDivisors(2, 4), [1, 2])

    def test_divisors(self):
        self.assertEqual(el.divisors(4), [1, 2, 4])

    def test_factorize(self):
        self.assertEqual(el.factorize(6), [2, 3])

if __name__ == '__main__':
    unittest.main()