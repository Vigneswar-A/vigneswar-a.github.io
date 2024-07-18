class Disjoint:
    def __init__(self , size):
        self.root = [*range(size)]
        self.rank = [0] * size
        
    def find(self , x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self , x , y):
        rootx = self.find(x)
        rooty = self.find(y)
        
        if rootx == rooty:
            return False
        
        if self.rank[rootx] > self.rank[rooty]:
            self.root[rooty] = rootx
        
        elif self.rank[rooty] > self.root[rootx]:
            self.root[rootx] = rooty
            
        else:
            self.rank[rootx] += 1
            self.root[rootx] = rooty
        
        return True
            
class Solution:
    def minCostConnectPoints(self, p: List[List[int]]) -> int:
        n = len(p)
        edges = sorted((sum(abs(p[i][k] - p[j][k]) for k in [0 , 1]) , i , j) for i in range(n) for j in range(n) if i != j)
        
        
        graph = Disjoint(n)
        total = 0
        count = 0
        for edge in edges:
            if count == n - 1:
                break
            dist , x , y = edge
            if graph.union(x , y):
                total += dist
                count += 1       
                
        return total