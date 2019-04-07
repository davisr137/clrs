import math

class Heap(object):
    """
    Heap array class. 
    """
    def __init__(self, values, heap_size=None):
        """
        Initialize heap .
        
        Args:
            values (list of int): Values in heap..
            heap_size (int): Number of elements in the heap stored
                within the array. If None, set to len(A). 
        """
        self.values = values
        if heap_size is None:
            heap_size = len(values)
        self._heap_size = heap_size

    @property
    def heap_size(self):
        """
        Number of elements in the heap stored within the array.
        """
        return self._heap_size

    def exchange(self, i, j):
        """
        Swap elements at indices i and j of array.

        Args:
            i (int)
            j (int)
        """
        tmp = self.values[i]
        self.values[i] = self.values[j]
        self.values[j] = tmp

    def __len__(self):
        """
        Pass through length of underlying array.
        """
        return len(self.values)

def parent(i):
    """
    Get index of parent of node at index i.

    Args:
        i (int): Index of node.

    Returns:
        int: Index of parent
    """
    return math.floor(i/2)

def left(i):
    """
    Get index of left child of node at index i.

    Args:
        i (int): Index of node.

    Returns:
        int: Index of left child.
    """
    return 2*i+1

def right(i):
    """
    Get index of right child of node at index i.

    Args:
        i (int): Index of node.

    Returns:
        int: Index of right child.
    """
    return 2*i+2

def max_heapify(A, i):
    """
    Transform subtree A[i] of into a max-heap. The left and right subtrees
    of A[i] must be max-heaps.

    Args:
        A (Heap): Our heap.
        i (int): Index into array.

    Returns:
        list of int: Heap with subtree at A[i] satisfying the max-heap 
            property.
    """
    l = left(i) # Root of left subtree
    r = right(i) # Root of right subtree
    largest = i
    if l < A.heap_size and A.values[l] > A.values[i]:
        largest = l
    if r < A.heap_size and A.values[r] > A.values[largest]:
        largest = r
    if largest != i:
        # Swap value of node i with value of node largest. Node i
        # and its children now satisfy the max-heap property. Node largest
        # may now violate the max-heap property, so call max_heapify()
        # recursively on it.
        A.exchange(i, largest) 
        A = max_heapify(A, largest)
    return A

def build_max_heap(A):
    """
    Build a max-heap bottom-up from an unsorted array A.

    Args:
        A (Heap): Unsorted array.

    Returns:
        list of int: max-heap from elements of A
    """
    for i in reversed(range(0, math.floor(len(A)/2))):
        A = max_heapify(A, i)
    return A

def heapsort(A):
    """
    Sort array A using heapsort algorithm.

    Args:
        A (list of int): Unsorted array.
    
    Returns:
        list of int: Sorted array.
    """
    # Build a max-heap from input array.
    A = build_max_heap(A)
    l = len(A)
    heap_size = l
    for i in reversed(range(1, l)):
        A.exchange(0, i)
        A._heap_size -= 1
        A = max_heapify(A, 0)
    return A


class PriorityQueue(object):

    def __init__(self):
        pass

    def insert(self, x):
        pass

    def maximum(self):
        pass

    def extract_max(self):
        pass

    def increase_key(self, x, k):
        pass


