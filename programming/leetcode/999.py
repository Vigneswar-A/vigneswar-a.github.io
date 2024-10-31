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
            return True
        
        if self.rank[rootx] > self.rank[rooty]:
            self.root[rooty] = rootx
        elif self.rank[rooty] > self.rank[rootx]:
            self.root[rootx] = rooty
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1
            
    
        

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        uf = UnionFind((m*n+1)*4)
        
        def idx(i, j, d):
     
            directions = 'LTRB'
            box = (i*n+j)*4
            
            return box+directions.index(d)
            
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == '\\':
                    uf.union(idx(i, j, 'T'), idx(i, j, 'R'))
                    uf.union(idx(i, j, 'L'), idx(i, j, 'B'))
                elif grid[i][j] == '/':
                    uf.union(idx(i, j, 'T'), idx(i, j, 'L'))
                    uf.union(idx(i, j, 'B'), idx(i, j, 'R'))
                else:
                    uf.union(idx(i, j, 'T'), idx(i, j, 'L'))
                    uf.union(idx(i, j, 'B'), idx(i, j, 'R'))
                    uf.union(idx(i, j, 'T'), idx(i, j, 'R'))
                    uf.union(idx(i, j, 'L'), idx(i, j, 'B'))
                if i:            
                    uf.union(idx(i, j, 'T'), idx(i-1, j, 'B'))
                if j+1 < n:
                    uf.union(idx(i, j, 'R'), idx(i, j+1, 'L'))
                if j:
                    uf.union(idx(i, j, 'L'), idx(i, j-1, 'R'))
                if i+1 < m:
                    uf.union(idx(i, j, 'B'), idx(i+1, j, 'T'))
                    
        roots = set()
        for i in range(m):
            for j in range(n):
                for d in 'LRTB':
                    roots.add(uf.find(idx(i, j, d)))
        
                   
                
        return len(roots)
                
                   
                    
                
                    
                    
                    
                    
                
        