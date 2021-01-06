class Graph:
    # Adjacency list representation of the graph
    def __init__(self, V): #V is the number of vertices
        self.V = V
        self.adj = [[] for _ in range(V)]
    
    def add_edge(self, v, e): # Add edge e to vertex v
        self.adj[v].append(e)

    