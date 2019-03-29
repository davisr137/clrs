def insertion_sort(A):
    """
    Perform insertion sort on array A.
    
    Loop invariant: At the start of the for loop,
    the subarray A[1..j-1] consists of elements in 
    positions 1 through j-1, but in sorted order.
    """
    for i in range(1, len(A)):
        a = A[i]
        j = i-1
        while j >= 0 and A[j] > a:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = a
    return A

def add_binary_ints(A, B):
    """
    Add binary integers A and B. A and B are represented
    as lists of bools and must be of the same length.
    
    CLRS Exercise 2.1-4
    """
    l = len(A)
    c = [0]*(l+1)
    carry = 0
    for i in range(l):
        c[i] = (A[i] + B[i] + carry) % 2
        if A[i] + B[i] + carry > 1:
            carry = 1
        else:
            carry = 0
    c[l] = carry
    return c

