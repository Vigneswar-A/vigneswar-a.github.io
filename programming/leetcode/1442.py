class UnionFind:
    def __init__(self, n):
        self.root = [*range(n)]
        self.rank = [0]*n
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
        
    def union(self, u, v):
        x = self.find(u)
        y = self.find(v)
        if self.rank[x] > self.rank[y]:
            self.root[y] = x
        elif self.rank[y] > self.rank[x]:
            self.root[x] = y
        else:
            self.root[y] = x
            self.rank[x] += 1
            
            
    def is_connected(self, u, v):
        return self.find(u) == self.find(v)
    

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        uf = UnionFind(n)
        wires = 0
        connected = 0
        for u,v in connections:
            if uf.is_connected(u, v):
                wires += 1

            else:
                uf.union(u, v)
                wires += 1
                connected += 1
                
        return n-connected-1 if wires >= n-1 else -1
                
        
        
        