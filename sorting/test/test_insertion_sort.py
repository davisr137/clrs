import unittest2 as unittest
import clrs.sorting.insertion_sort as ist

class TestCase(unittest.TestCase):
    """
    Test code from insertion sort section. 
    """
    def test_insertion_sort(self):
        """
        Test insertion sort algorithm.
        """
        unsorted_arrs = [[1, 7, 5, 3], [7, 3, 1], [7, 7, 8, 8, 1, 1, 3]]
        sorted_arrs = [[1, 3, 5, 7], [1, 3, 7], [1, 1, 3, 7, 7, 8, 8]]
        for i in range(len(unsorted_arrs)):
            self.assertEqual(ist.insertion_sort(unsorted_arrs[i]), sorted_arrs[i])
    
    def test_add_binary_ints(self):            
        """
        Add binary integers.
        """
        A = [1, 1, 1]
        B = [1, 1, 1]
        C = [0, 1, 1, 1]
        self.assertEqual(ist.add_binary_ints(A, B), C)
