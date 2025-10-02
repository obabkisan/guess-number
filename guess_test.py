import unittest

from guess import guess_number


class TestMath(unittest.TestCase):
    def test_seq_search_success(self):
        """проверка медленного поиска при успешной находке числа"""
        sself.assertEqual(guess_number(5, [1, 2, 3, 4, 5, 6, 7], 'seq'), (5, 5))

    def test_seq_search_outside_range(self):
        """проверка медленного поиска при отсутствии числа в списке"""
        self.assertEqual(guess_number(10, [1, 2, 3, 4, 5, 6, 7], 'seq'), (-1, 7))

    def test_bin_search_success(self):
        """проверка бинарного поиска при успешной находке числа"""
        self.assertEqual(guess_number(5, [1, 2, 3, 4, 5, 6, 7], 'bin'), (5, 3))

    def test_bin_search_outside_range(self):
        """проверка бинарного поиска при отсутствии числа в списке"""
        self.assertEqual(guess_number(10, [1, 2, 3, 4, 5, 6, 7], 'bin'), (-1, 3))

    def test_seq_search_boundary_left(self):
        """проверка медленного поиска числа на левом крае диапазона"""
        self.assertEqual(guess_number(1, [1, 2, 3, 4, 5, 6, 7], 'seq'), (1, 1))

    def test_bin_search_boundary_right(self):
        """проверка бинарного поиска числа на правом крае диапазона"""
        self.assertEqual(guess_number(7, [1, 2, 3, 4, 5, 6, 7], 'bin'), (7, 3))


if __name__ == '__main__':
    unittest.main()
