
import unittest

from bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        unsorted_list = [66, 11, 48, 1, 70]
        expected_list = [1, 11, 48, 66, 70]

        unsorted_list = bubble_sort(unsorted_list)
        print(unsorted_list)
        self.assertEqual(unsorted_list, expected_list)


if __name__ == '__main__':
    unittest.main()
