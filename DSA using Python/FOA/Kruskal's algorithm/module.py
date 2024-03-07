print("Priyanka Tiwari : 1000")
class DisjointSet:
    def __init__(self, vertices):
        self.parent = [i for i in range(vertices)]
        self.rank = [0] * vertices
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)

        if self.rank[rootU] > self.rank[rootV]:
            self.parent[rootV] = rootU
        elif self.rank[rootU] < self.rank[rootV]:
            self.parent[rootU] = rootV
        else:
            self.parent[rootV] = rootU
            self.rank[rootU] += 1

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append([u, v, weight])

    def kruskal(self):
        self.graph = sorted(self.graph, key=lambda item: item[2])
        mst = []
        ds = DisjointSet(self.V)

        for edge in self.graph:
            u, v, weight = edge
            if ds.find(u) != ds.find(v):
                mst.append([u, v, weight])
                ds.union(u, v)

        return mst

# Example usage
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)
minimum_spanning_tree = g.kruskal()
print("Edges in the Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge[0], "-", edge[1], ":", edge[2])
