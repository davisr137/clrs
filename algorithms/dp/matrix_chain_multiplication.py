from typing import List

# CLRS Section 15.2
# Matrix-chain multiplication

INF = 10**30

def matrix_chain_order(p: List[int]):
    """
    Build tables using a bottom up approach to find the 
    minimum number of scalar multiplications for a matrix 
    chain. 

    Returns:
        m -> m[i,j] is the minimum number of scalar multiplications
            needed to compute the matrix A_{i..j}
        s -> s[i,j] is the value of k such that 
            m[i,j] = m[i,k] + m[k+1, j] +p_{i-1}*p_k*p_j
    """
    # n is the number of matrices to multiply
    n = len(p) - 1
    # Initialize m, s with None
    m = []
    s = []
    for i in range(n):
        m += [[None] * n]
        s += [[None] * n]
    # For chains consisting of one matrix, m[i,i] = 0
    for i in range(n):
        m[i][i] = 0
    # l is the chain lengths
    for l in range(2, n+1):
        # i is the start index of chain 
        for i in range(n-l+1):
            # j is the end index of the chain
            j = i + l - 1 
            # Initialize # scalar mult to large value
            m[i][j] = INF
            # Find value of k that minimizes scalar mults
            for k in range(i, j):
                # Compute # scalar mults
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                # Update best solution
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return [m, s]

def print_array(array: List[List[int]]):
    """
    Print each line in array one at a time.
    """
    for line in array:
        print(line)
