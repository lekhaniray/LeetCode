import unittest
from reverseInteger import Solution
from JewelsStones import Solution1

class reverseIntegerTest(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(Solution.reverse1(321), 123)
        self.assertEqual(Solution.reverse1(789), 987)

    def test_Jewel(self):
        self.assertEqual(Solution1.numJewelsInStones("aA", "aAAbbbb"), 3)


if __name__ == '__main__':
    unittest.main()
