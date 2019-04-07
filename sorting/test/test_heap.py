import unittest2 as unittest
import clrs.sorting.heap as heap

class TestHeap(unittest.TestCase):
    """
    Unit tests for heap code.
    """
    def test_max_heapify(self):
        """
        Transform.values with max-heap subtrees into
        a max-heap.
        """
        A = heap.Heap([16, 4, 10, 14, 7, 9, 3, 2, 8, 1])
        A_mh = heap.max_heapify(A, 1).values
        self.assertEqual(A_mh, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

    def test_build_max_heap(self):
        """
        Build max heap from unsorted.values.
        """
        A = heap.Heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
        A_mh = heap.build_max_heap(A).values
        self.assertEqual(A_mh, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

    def test_heapsort(self):
        """
        Sort.values using heapsort.
        """
        A = heap.Heap([1,4,6,7,8,2,3,4,5,7])
        A_st = heap.heapsort(A).values
        self.assertEqual(A_st, [1, 2, 3, 4, 4, 5, 6, 7, 7, 8])

class TestPriorityQueue(unittest.TestCase):
    """
    Unit tests for priority queue class.
    """
    def setUp(self):
        """
        Initialize PQ.
        """
        self.pq = heap.PriorityQueue([15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1])

    def test_extract_max(self):
        """
        Extract max from PQ.
        """
        _max = self.pq.extract_max()
        self.assertEqual(_max, 15)
        self.assertEqual(self.pq.A.values, [13, 12, 9, 5, 6, 8, 7, 4, 0, 1, 2, 1])

    def test_insert(self):
        """
        Insert new element into PQ.
        """
        self.pq.insert(10)
        self.assertEqual(self.pq.A.values, [15, 13, 10, 5, 12, 9, 7, 4, 0, 6, 2, 1, 8])
