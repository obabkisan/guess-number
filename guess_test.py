import unittest

from guess import guess_number


class TestMath(unittest.TestCase):
    def test_seq_search_success(self):
        """проверка медленного поиска при успешной находке числа"""
        result, attempts = guess_number(5, [1, 2, 3, 4, 5, 6, 7], 'seq')
        sself.assertEqual((result, attempts), (5, 5))

    def test_seq_search_outside_range(self):
        """проверка медленного поиска при отсутствии числа в списке"""
        result, attempts = guess_number(10, [1, 2, 3, 4, 5, 6, 7], 'seq')
        self.assertEqual((result, attempts), (-1, 7))

    def test_bin_search_success(self):
        """проверка бинарного поиска при успешной находке числа"""
        result, attempts = guess_number(5, [1, 2, 3, 4, 5, 6, 7], 'bin')
        self.assertEqual((result, attempts), (5, 3))

    def test_bin_search_outside_range(self):
        """проверка бинарного поиска при отсутствии числа в списке"""
        result, attempts = guess_number(10, [1, 2, 3, 4, 5, 6, 7], 'bin')
        self.assertEqual((result, attempts), (-1, 3))

    def test_seq_search_boundary_left(self):
        """проверка медленного поиска числа на левом крае диапазона"""
        result, attempts = guess_number(1, [1, 2, 3, 4, 5, 6, 7], 'seq')
        self.assertEqual((result, attempts), (1, 1))

    def test_bin_search_boundary_right(self):
        """проверка бинарного поиска числа на правом крае диапазона"""
        result, attempts = guess_number(7, [1, 2, 3, 4, 5, 6, 7], 'bin')
        self.assertEqual((result, attempts), (7, 3))


if __name__ == '__main__':
    unittest.main()
