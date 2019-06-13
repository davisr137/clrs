from typing import List, Dict

## CLRS Section 22: Graph Algorithms

## Section 22.1 Representation of Graphs

def adjacency_list_from_matrix(M: List[List[int]]) -> List[List[int]]:
    """
    Convert an adjacency matrix representation of a graph
    to an adjacency list representation.
    """
    # V is the number of vertices
    V = len(M)
    A = []
    for i in range(V):
        # Adjacency list for vertex i
        Ai = []
        for j in range(V):
            if M[i][j]:
                Ai += [j+1]
        A += [Ai]
    return A

def adjacency_matrix_from_list(A: List[List[int]]) -> List[List[int]]:
    """
    Convert an adjacency matrix representation of a graph to an 
    adjacency list representation.
    """
    # V is the number of vertices
    V = len(A)
    # Make matrix of all zeros
    M = []
    for _ in range(V):
        M += [[0] * V]
    # Add 1 to matrix for edge
    for i, l in enumerate(A):
        for j in l:
            M[i][j-1] = 1
    return M

## Section 22.2 Breadth-First Search

class Node:
    """
    Class for node in graph
    """
    def __init__(self, value):
        self.value = value
        self.color = None
        self.distance = None
        self.predecessor = None
    def __repr__(self):
        return self.value
    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.value == other.value
    def __hash__(self):
        return hash(self.value)

class Graph:
    def __init__(self, adj: Dict):
        """
        Initialize graph using adjacency list representation
        stored in dictionary.
        """
        keys = list(adj.keys())
        # Map node values to pointers to Node objects
        nodes = {}
        for key in keys:
            nodes[key] = Node(key)
        self.nodes = nodes
        # Make new adjacency list with Node objects
        adjD = {}
        for key in keys:
            adjD[nodes[key]] = [nodes[label] for label in adj[key]]
        self.adj = adjD

class Queue:
    """
    Class for queue (FIFO).
    """
    def __init__(self):
        self.Q = []
    def enqueue(self, node: Node):
        self.Q = [node] + self.Q
    def dequeue(self) -> Node:
        return self.Q.pop()
    def is_empty(self) -> bool:
        return len(self.Q) == 0

def bfs(G: Graph, s: Node):
    """
    Perform breadth-first search on graph G starting at source node s.
    """
    # Color non-source vertices white
    for node in G.adj:
        if node is not s:
            node.color = 'W'
            node.distance = 100
    # Color source gray, distance=0, no predecessor
    s.color = 'G'
    s.distance = 0
    # Initialize queue with only source
    Q = Queue()
    Q.enqueue(s)
    # Explore while there may be unexplored vertices / nodes
    while not Q.is_empty():
        u = Q.dequeue()
        adj = G.adj[u]
        for v in adj:
            if v.color == 'W':
                v.color = 'G'
                v.distance = u.distance + 1
                v.predecessor = u
                Q.enqueue(v)
        u.color = 'B'
