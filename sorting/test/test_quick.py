import unittest2 as unittest 
import clrs.sorting.quick as qs

class TestQuicksort(unittest.TestCase):
    """
    Test quicksort code.
    """
    @classmethod
    def setUpClass(cls):
        """
        Initialize array for tests.
        """
        cls.A = [2, 8, 7, 1, 3, 5, 6, 4]

    def test_partition(self):
        """
        Partition in place.
        """
        [B, pivot] = qs.partition(self.A, 0, len(self.A)-1)
        self.assertEqual(B, [2, 1, 3, 4, 7, 5, 6, 8])
        self.assertEqual(pivot, 3)

    def test_quicksort(self):
        """
        Run quicksort algorithm.
        """
        B = qs.quicksort(self.A, 0, 7)
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])
