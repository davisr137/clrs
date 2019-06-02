import numpy as np
from typing import List

## CLRS Section 15.2
## Matrix-chain multiplication

# We have a sequence (chain) [A1, A2,...,An] of matrices and we 
# want to compute the product A1A2...An. A product of matrices 
# is fully parenthesized if it is either a single matrix or the
# product of two fully parenthesized matrix products, surrounded
# by parentheses. We want to find the arrangement of parentheses
# such that the number of scalar multiplications is minimized.

INF = 10**30

def matrix_chain_order(p: List[int]) -> List:
    """
    Build tables using a bottom up approach to find the 
    minimum number of scalar multiplications for a matrix 
    chain. 

    Args:
        p (list of int): Dimensions of matrices in order.

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

def get_optimal_parens(s: List[List[int]], i: int, j: int, op: str) -> str:
    """
    Print optimal parenthesization of chain matrix product.

    Args:
        s (list of list of int): s[i,j] is the value of k such that
            the optimal parenthesization splits the product between A_k
            and A_{k+1}
        i (int) : Start index in matrix chain.
        j (int) : End index in matrix chain.
    
    Returns:
        str - Printed optimal parenthesization of matrices.
    """
    if i == j:
        op += 'A%s' % i
        return op
    op += '('
    op = get_optimal_parens(s, i, s[i][j], op)
    op = get_optimal_parens(s, s[i][j]+1, j, op)
    op += ')'
    return op

def generate_matrices(p: List[int]) -> List[np.ndarray]:
    """
    Generate a list of matrices from a list of dimensions p. Each 
    matrix is all ones.
    """
    matrices = []
    L = len(p)
    for i in range(1, L):
        matrices += [np.ones((p[i-1], p[i]))]
    return matrices

## Exercise 15.2-2

def matrix_chain_multiply(A: List[np.ndarray], s: List[List[int]], i: int, j: int) -> np.ndarray:
    """
    Multiply chain of matrices as to minimize the number of scalar operations.

    Args:
        A (list of np.ndarray): Our matrices to multiply.
        s (list of list of int): s[i,j] is the value of k such that
            the optimal parenthesization splits the product between A_k
            and A_{k+1}
        i (int) : Start index in matrix chain.
        j (int) : End index in matrix chain.

    Returns:
        np.ndarray: Product of matrices.
    """
    if i == j:
        return A[i]
    if i + 1 == j:
        return np.dot(A[i], A[j])
    Ak = matrix_chain_multiply(A, s, i, s[i][j])
    Ak1 = matrix_chain_multiply(A, s, s[i][j]+1, j)
    prod = np.dot(Ak, Ak1)
    return prod
