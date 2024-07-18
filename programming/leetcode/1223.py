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
        
        if rootx  == rooty:
            return 
        
        if self.rank[rootx] > self.rank[rooty]:
            self.root[rooty] = rootx
            
        elif self.rank[rooty] > self.rank[rootx]:
            self.root[rootx] = rooty
            
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        visited = [0]*n
        uf = UnionFind(n)
        
        for i in range(1, n+1):
            if visited[i-1]:
                continue
            if i > threshold:
                for j in range(i, n+1, i):
                    uf.union(i-1, j-1)
                    visited[j-1] = 1

        return [uf.connected(u-1, v-1) for u,v in queries]

        
                
            
        
        