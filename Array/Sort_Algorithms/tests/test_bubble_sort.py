import unittest
from array import array
from bubble_sort import bubble_sort as sort_function

class TestSort(unittest.TestCase):

    def test_array(self):
        test_data = array('i', [20, 35, -15, 7, 55, 1, -22])
        result = array('i', [-22, -15, 1, 7, 20, 35, 55])
        sort_function(test_data)
        self.assertEqual(test_data, result)