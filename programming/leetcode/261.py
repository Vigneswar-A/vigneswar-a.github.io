class Disjoint:
    def __init__(self , n):
        self.root = [*range(n)]
        self.rank = [1] * n
        
    def find(self , x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self , x , y):
        x , y = map(self.find , (x , y))
        if x == y:
            return False
        
        if self.rank[x] > self.rank[y]:
            self.root[y] = x
        elif self.rank[x] == self.rank[y]:
            self.rank[x] += 1
            self.root[y] = x
        else:
            self.root[x] = y
            
        return True
    
    def clean(self):
        for i in range(len(self.root)):
            if self.root[i] != i:
                self.find(i)
                
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = Disjoint(n)
        
        for u , v in edges:
            if not graph.union(u , v):
                return False
            
        graph.clean()
        return len(set(graph.root)) == 1
        