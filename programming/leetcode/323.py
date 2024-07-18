class UnionFind:
    def __init__(self , size):
        self.root = [*range(size)]
        self.rank = [1] * size
        
    def find(self , x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
        
    def union(self , x , y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return False
        
        if self.rank[x] > self.rank[y]:
            self.root[y] = x
            
        elif self.rank[x] < self.rank[y]:
            self.root[x] = y
            
        else:
            self.rank[x] += 1
            self.root[y] = x
            
        return True
    
    def clean(self):
        for i in range(len(self.root)):
            self.root[i] = self.find(i)
            
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = UnionFind(n)
        
        for u,v in edges:
            graph.union(u , v)
            
        graph.clean()
        
        return len(set(graph.root))
        
        