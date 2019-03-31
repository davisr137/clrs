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

    def test_merge_sort(self):
        """
        Sort an array with merge sort.
        """
        A = [5, 2, 4, 7, 1, 3, 2, 6]
        A_sorted = mst.merge_sort(A, 0, 8)
        self.assertEqual(A_sorted, [1, 2, 2, 3, 4, 5, 6, 7])

    def test_merge_sort_no_sentinels(self):

        A = [1,4,6,7,8,2,3,4,5,7,10,15,25,30,35]
        A_sorted = mst.merge_no_sentinels(A, 0, 5, 15)
        self.assertEqual(A_sorted, sorted(A))


