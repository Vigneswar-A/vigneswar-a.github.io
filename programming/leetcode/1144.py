class UnionFind:
    def __init__(self, n):
        self.root = [*range(n)]
        self.rank = [0]*n
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        
        if rootx == rooty:
            return 0
        
        if self.rank[rootx] > self.rank[rooty]:
            self.root[rooty] = rootx
        elif self.rank[rooty] > self.rank[rootx]:
            self.root[rootx] = rooty
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1  
        
        return 1

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        
        edges = []
        for u,v,c in pipes:
            edges.append((c, u, v))
            
        for i in range(1, len(wells)+1):
            edges.append((wells[i-1], i, 0))

        res = 0
        uf = UnionFind(n+1)
        for c, u, v in sorted(edges):
            if uf.union(u, v):
                res += c
                n -= 1
                
            if n == -1: break
                
        return res
    
            
            
        
        