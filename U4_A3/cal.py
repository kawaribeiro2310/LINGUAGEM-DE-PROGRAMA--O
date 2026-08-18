# assert

def sum_numbers(numbers):
    return sum(numbers)


assert sum_numbers([1, 2, 3, 4]) == 10
assert sum_numbers([-1, 0, 1]) == 0
assert sum_numbers([]) == 0

print("asserts OK")


# doctest

def sum_numbers_doc(numbers):
    """Soma os números em uma lista.

    Exemplos:
    >>> sum_numbers_doc([1, 2, 3, 4])
    10
    >>> sum_numbers_doc([-1, 0, 1])
    0
    >>> sum_numbers_doc([])
    0
    """
    return sum(numbers)


# unittest
import unittest


class TestSumNumbers(unittest.TestCase):
    def test_sum_numbers_positive(self):
        self.assertEqual(sum_numbers([1, 2, 3, 4]), 10)

    def test_sum_numbers_mixed(self):
        self.assertEqual(sum_numbers([-1, 0, 1]), 0)

    def test_sum_numbers_empty(self):
        self.assertEqual(sum_numbers([]), 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)