import copy
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
        # 'discovered' and 'finished' fields used for DFS
        self.discovered = None
        self.finished = None
    def __repr__(self):
        return self.value
    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.value == other.value
    def __hash__(self):
        return hash(self.value)

def dict_str_to_dict_node(d_str: Dict) -> Dict:
    """
    Convert dict with keys and values as str to dict
    with keys and values as Node.
    """
    keys = list(d_str.keys())
    nodes = {}
    for key in keys:
        nodes[key] = Node(key)
    d_node = {}
    for key in keys:
        d_node[nodes[key]] = [nodes[label] for label in d_str[key]]
    return d_node

class Graph:
    def __init__(self, adj: Dict):
        """
        Initialize graph using adjacency list representation
        stored in dictionary.
        """
        self.adj = adj
        nodes_list = list(adj.keys())
        nodes = {}
        for node in nodes_list:
            nodes[node.value] = node
        self.nodes = nodes
    @classmethod
    def from_strings(cls, adj_str: Dict):
        """
        Initialize graph from dictionary of strings.
        """
        adj = dict_str_to_dict_node(adj_str)
        return cls(adj)

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

def bfs(G: Graph, s: Node) -> None:
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

def print_path(G: Graph, s: Node, v: Node):
    """
    Print the vertices on the shortest path from s to v, assuming BFS has
    already been run to compute the shortest-path tree.
    """
    if v == s:
        print(s)
    elif not v.predecessor:
        print("No path from %s to %s exists" % (s, v))
    else:
        print_path(G, s, v.predecessor)
        print(v)

## Section 22.3 Depth-First Search

def dfs(G: Graph) -> None:
    """
    Perform depth-first search on graph G.
    """
    # At beginning color all nodes white
    for key in G.nodes:
        G.nodes[key].color = 'W'
    # Use t for timestamping
    t = 0
    # Iterate over nodes, search if node not
    # discovered.
    for key in sorted(G.nodes):
        u = G.nodes[key]
        if u.color == 'W':
            dfs_visit(G, u, t)

def dfs_visit(G: Graph, u: Node, t: int) -> int:
    """
    Visit node u in depth-first search.
    """
    # Color node gray to mark discovery
    u.color = 'G'
    # Increment time
    t += 1
    u.discovered = t
    # Explore edge (u, v)
    for v in sorted(G.adj[u], key = lambda v:v.value):
        if v.color == 'W':
            v.predecessor = u
            t = dfs_visit(G, v, t)
    # Color u black; it is finished
    u.color = 'B'
    t += 1
    u.finished = t
    return t

## Detect a cycle in a graph using DFS

def cycle(G: Graph) -> bool:
    """
    Return True if graph G has a cycle, else return False.
    """
    # At beginning color all nodes white
    for key in G.nodes:
        G.nodes[key].color = 'W'
    # Search undiscovered nodes
    for key in sorted(G.nodes):
        u = G.nodes[key]
        # Graph has a back edge - there is a cycle!
        if u.color == 'G':
            return True
        if u.color == 'W':
            found_cycle = dfs_visit_cycle(G, u)
            if found_cycle:
                return True
    return False

def dfs_visit_cycle(G: Graph, u: Node) -> bool:
    """
    Visit node u in depth-first search.
    """
    # Color node gray to mark discovery
    u.color = 'G'
    # Explore edge (u, v)
    for v in sorted(G.adj[u], key = lambda v : v.value):
        if v.color == 'G':
            return True
        if v.color == 'W':
            v.predecessor = u
            found_cycle = dfs_visit_cycle(G, v)
            if found_cycle:
                return True
    # Color u black; it is finished
    u.color = 'B'
    return False

## Section 22.4: Topological sort

def topological_sort_visit(G: Graph, u: Node, t: int, L: List) -> List:
    """
    Visit node u as part of a topological sort. 
    """
    u.color = 'G'
    t += 1
    u.discovered = t
    for v in sorted(G.adj[u], key = lambda v:v.value):
        if v.color == 'W':
            v.predecessor = u
            [t, L] = topological_sort_visit(G, v, t, L)
    u.color = 'B'
    t += 1
    u.finished = t
    L = [u] + L
    return [t, L]

def topological_sort(G: Graph) -> List:
    """
    Perform a topological sort on graph G. Return a list of
    nodes in topologically sorted order. 
    """
    # At beginning color all nodes white
    for key in G.nodes:
        G.nodes[key].color = 'W'
    # Use t for timestamping
    t = 0
    L = []
    # Iterate over nodes, search if node not
    # discovered.
    for key in sorted(G.nodes):
        u = G.nodes[key]
        if u.color == 'W':
            [t, L] = topological_sort_visit(G, u, t, L)
    return L

## Section 22.5: Strongly connected components

def transpose(G: Graph) -> Graph:
    """
    Return the transpose of a graph G consisting of the edges
    of G with their directions reversed.
    """
    adj = copy.deepcopy(G.adj)
    adj_tr = {}
    for node in adj:
        adj_tr[node] = []
    for node in adj:
        adj_nodes = adj[node]
        for adj_node in adj_nodes:
            adj_tr[adj_node] += [node]
    GT = Graph(adj_tr) 
    return GT

def strongly_connected_components(G: Graph):
    """
    Compute the strongly connected components of a graph G. A 
    strongly connected component is a maximal set of vertices C
    such that for every pair of vertices u and v in C, u and v
    are reachable from each other.
    """
    # Run DFS and get finishing times (f)
    dfs(G)
    # Compute transpose
    GT = transpose(G)
    # Run DFS but consider the vertices in order of decreasing f
