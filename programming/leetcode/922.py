class UnionFind:
    def __init__(self, n):
        self.root = [*range(n)]
        self.rank = [1]*n

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return 
        
        if self.rank[rootx] > self.rank[rooty]:
            self.root[rooty] = rootx
        elif self.rank[rooty] > self.rank[rootx]:
            self.root[rootx] = rooty
        else:
            self.rank[rootx] += 1
            self.root[rooty] = rootx

    
    def isconnected(self, x, y):
        return self.find(x) == self.find(y)
            
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        adj = [[] for _ in range(n+1)]

        for u,v in dislikes:
            adj[u].append(v)
            adj[v].append(u)

        graph = UnionFind(n+1)
        for node in range(n):
            for nei in adj[node]:
                if graph.isconnected(node, nei):
                    return False
                graph.union(adj[node][0], nei)

        return True

        

