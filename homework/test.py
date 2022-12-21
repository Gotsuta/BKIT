import unittest
from cpn import cpn_gen
from collections.abc import Generator
from functools import reduce

class TestCPN(unittest.TestCase):
    def test_generator(self):
        sequence = cpn_gen()
        self.assertIsInstance(sequence, Generator)

        self.assertEqual(next(sequence), 1)
        self.assertEqual(next(sequence), 2)
        self.assertEqual(next(sequence), 4)

    def test_sequence(self):
        gen = cpn_gen()
        sequence = [next(gen) for _ in range(8)]
        self.assertEqual(len(sequence), 8)
        self.assertListEqual(sequence, [1, 2, 4, 7, 11, 16, 22, 29])

        exp = [37, 46]
        for ind, val in enumerate(gen):
            if ind > 1:
                break
            self.assertEqual(val, exp[ind])

    def test_func(self):
        gen = cpn_gen()
        sequence = list(zip(range(6), gen))
        self.assertEqual(len(sequence), 6)
        self.assertListEqual(sequence, [(0, 1), (1, 2), (2, 4), (3, 7), (4, 11), (5, 16)])

        sequence = list(zip(range(6), gen))
        self.assertEqual(len(sequence), 6)
        self.assertListEqual(sequence, [(0, 22), (1, 29), (2, 37), (3, 46), (4, 56), (5, 67)])


if __name__ == "__main__":
    unittest.main()