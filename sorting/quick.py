
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
        [A, i]
            A (list of int) is array with subarray sorted.
            i is the index of the pivot.
    """
    x = A[r]
    i = p-1
    for j in range(p, r-1):
        if A[j] <= x:
            i += 1
            A = exchange(A, i, j)
    A = exchange(A, i+1, r)
    return [A, i+1]
