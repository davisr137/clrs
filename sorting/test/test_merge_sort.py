import unittest2 as unittest
import clrs.sorting.merge_sort as mst

class TestCase(unittest.TestCase):
    """
    Test code from merge sort section. 
    """
    def test_merge(self):
        """
        Merge two sorted sub-arrays into a single sorted array.
        """
        A = [1,4,6,7,8,2,3,4,5,7]
        p = 0
        q = 5
        r = 10
        A_merged = mst.merge(A, p, q, r)
        expected = [1, 2, 3, 4, 4, 5, 6, 7, 7, 8] 
        self.assertEqual(A, A_merged)
