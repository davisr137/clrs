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
