class UnionFind:
    def __init__(self , n):
        self.root = [*range(0 , n + 1)]
    
    def find(self , x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self , x , y):
        if self.root[self.find(y)] == self.root[self.find(x)]:
            return True
        self.root[self.find(y)] = self.root[self.find(x)]
        
    def isconnected(self , x , y):
        return self.root[x] == self.root[y]
        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = UnionFind(n)
        for u , v in edges:
            if graph.union(u, v):
                return [u , v]

        
        
