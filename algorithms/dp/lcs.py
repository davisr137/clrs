from typing import List

## CLRS Section 15.4 - Longest common subequence

def empty_grid(m: int, n: int, zero: bool=True) -> List[List]: 
    """
    Make an empty m x n grid.
    """
    G = []
    for _ in range(m):
        if zero:
            G += [[0] * n]
        else:
            G += [[''] * n]
    return G

def lcs_length(X: str, Y: str) -> List:
    """
    Get tables finding longest common subsequence for strings 
    X and Y.
    """
    m = len(X)
    n = len(Y)
    # Make empty grids for c and b. c[i][j] is the length of
    # a LCS of Xi and Yj.
    c = empty_grid(m+1, n+1)
    # b shows how to recover the characters in the LCS
    b = empty_grid(m+1, n+1, zero=False)
    # LCS is zero if one string has zero length
    for i in range(m+1):
        c[i][0] = 0
    for j in range(n+1):
        c[0][j] = 0
    # Iterate over rows, then columns
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 'LU'
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 'U'
            else: # c[i-1][j] < c[i][j-1]
                c[i][j] = c[i][j-1]
                b[i][j] = 'L'
    return [c,b]

def lcs_string(b: List[List[int]], X: str) -> str:
    """
    Get longest common substring from b.
    """
    m = len(b)
    n = len(b[0])
    i = m-1
    j = n-1
    s = ""
    while i > 1 or j > 1:
        char = b[i][j]
        if char == 'LU':
            s += X[i-1]
            i -= 1
            j -= 1
        elif char == 'U':
            i -= 1
        elif char == 'L':
            j -= 1
    return s[::-1]

## Exercise 15.4-2

def lcs_string_c(c: List[List[int]], X: str, Y: str) -> str:
    """
    Reconstruct a LCS from the completed c table and original
    strings X and Y in O(m+n) time without using the b table.
    """
    m = len(c)
    n = len(c[0])
    i = m-1
    j = n-1
    s = ""
    while i > 1 or j > 1:
        if X[i-1] == Y[j-1]:
            s += X[i-1]
            i -= 1
            j -= 1
        elif c[i-1][j] >= c[i][j-1]:
            i -= 1
        else:
            j -= 1
    return s[::-1]

## Exercise 15.4-4
## Show how to compute the length of a LCS using only 2 * min(m, n)
## entries in the c table plus O(1) additional space. Then show how 
## to do this using min(m, n) entries plus O(1) additional space.

## Only need to keep min(m, n) + 1 records (Z) stored in c at a time. LCS
## length algorithm goes one row at a time. Choose whichever (X, Y) 
## is longer to be represented by rows, and the smaller to be 
## represented by columns. c[i-1][j-1] -> Z[0], c[i][j-1] -> Z[-1],
## c[i-1][j] -> Z[1]


