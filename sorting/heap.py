import math

class Array(object):

    def __init__(self, A, heap_size):
        self.array = A
        self._heap_size = heap_size

    @property
    def heap_size(self):
        return self._heap_size

    @property
    def length(self):
        return len(self.array)

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

def exchange(A, i, j):
    """
    Swap elements at indices i and j of array A.

    Args:
        A (list of int)
        i (int)
        j (int)

    Returns:
        list of int: Array with elements swapped.
    """
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp
    return A

def max_heapify(A, i):
    """
    Transform subtree A[i] of into a max-heap. The left and right subtrees
    of A[i] must be max-heaps.

    Args:
        A (list of int): Our array
        i (int): Index into array.

    Returns:
        list of int: Array with subtree at A[i] satisfying the max-heap 
            property.
    """
    l = left(i) # Root of left subtree
    r = right(i) # Root of right subtree
    largest = i
    if l <= len(A) and A[l] > A[i]:
        largest = l
    if r <= len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        # Swap value of node i with value of node largest. Node i
        # and its children now satisfy the max-heap property. Node largest
        # may now violate the max-heap property, so call max_heapify()
        # recursively on it.
        A = exchange(A, i, largest) 
        A = max_heapify(A, largest)
    return A
