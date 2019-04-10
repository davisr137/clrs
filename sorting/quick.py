
def exchange(A, i, j):
    """
    Swap elements at indices i and j of array.
    
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

def partition(A, p, r):
    """
    Partition subarray A[p...r] in place.

    Args:
        A (list of int): Our array.
        p (int): Starting index.
        r (int): Ending index.

    Returns:
        [A, q]
            A (list of int) is array with subarray sorted.
            q is the index of the pivot.
    """
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A = exchange(A, i, j)
    A = exchange(A, i+1, r)
    return [A, i+1]

def quicksort(A, p, r):
    """
    Implement quicksort algorithm.

    Args:
        A (list of int): Our array.
        p (int): Starting index.
        r (int): Ending index.
    """
    if p < r:
        [A, q] = partition(A, p, r)
        A = quicksort(A, p, q-1)
        A = quicksort(A, q+1, r)
    return A

