import unittest2 as unittest
import clrs.sorting.heap as heap

class TestCase(unittest.TestCase):
    """
    Unit tests for heap code.
    """
    def test_max_heapify(self):
        """
        Transform array with max-heap subtrees into
        a max-heap.
        """
        A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        A_mh = heap.max_heapify(A, 1)
        self.assertEqual(A_mh, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

    def test_build_max_heap(self):
        """
        Build max heap from unsorted array.
        """
        A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        A_mh = heap.build_max_heap(A)
        self.assertEqual(A_mh, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
