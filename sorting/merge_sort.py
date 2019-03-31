import math

# The sentinel is a value larger than any other possible 
# value in an array. Once we have reached the sentinel 
# in a sorted array, we have reached the end. 
SENTINEL = 10**10

def merge(A, p, q, r):
    """
    Merge sorted sub-arrays A[p:q] and A[q:r] of array A.

    Args:
        A (list of int): Our array.
        p (int)
        q (int)
        r (int)

    Returns:
        list of int: Sorted array.
    """
    L = A[p:q]
    R = A[q:r]
    L.append(SENTINEL)
    R.append(SENTINEL)
    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A

def merge_sort(A, p, r):
    """
    Perform merge sort on sub-array of array A between 
    elements indexed p and r. 

    Args:
        A (list of int): Our array.
        p (int)
        r (int)

    Returns: 
        A (list of int): Sorted array.
    """
    # Stop if we have a length-1 array -> already sorted
    if p < r-1:
        # Partition into two subarrays and merge each separately. 
        q = int(math.floor((p+r) / 2.0)) 
        A = merge_sort(A, p, q)
        A = merge_sort(A, q, r)
        # Merge the sorted sub-arrays.
        A = merge(A, p, q, r)
    return A

def merge_no_sentinels(A, p, q, r):
    """
    Merge sorted sub-arrays A[p:q] and A[q:r] of array A 
    without using sentinels.

    Args:
        A (list of int): Our array.
        p (int)
        q (int)
        r (int)

    Returns:
        list of int: Sorted array.

    CLRS Exercise 2.3-2
    """
    L = A[p:q]
    R = A[q:r]
    k = 0
    # Copy to A until L or R has all its elements copied back 
    # to A
    while L and R:
        if L[0] <= R[0]:
            A[k] = L.pop(0)
        else:
            A[k] = R.pop(0)
        k += 1
    # Copy the remainder of the non-empty back to A.
    if L:
        A[k:] = L
    elif R:
        A[k:] = R
    return A

