from typing import List

# CLRS Section 15.2

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
    # Initialize m with None
    m = []
    for i in range(n):
        m += [[None] * n]
    # For chains consisting of one matrix, m[i,i] = 0
    for i in range(n):
        m[i][i] = 0
    # l is the chain lengths
    for l in range(1, n):
        # i is the start of chain 
        for i in range(n-l+1):
            pass
