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
