class UnionFind:
    def __init__(self, n):
        self.root = [*range(n)]
        self.rank = [0]*n
        
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        
        if rootx == rooty:
            return False
        
        if self.rank[rootx] > self.rank[rooty]:
            self.root[rooty] = rootx
        elif self.rank[rooty] > self.rank[rootx]:
            self.root[rootx] = rooty
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1
            
    def clean(self):
        for i in range(len(self.root)):
            self.root[i] = self.find(i)
            
        
class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UnionFind(n*n)
        total = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == -1:
                    continue
                total += grid[i][j]
                for dx,dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                    if 0 <= i+dx < n and 0 <= j+dy < n and grid[i+dx][j+dy] != -1:
                        uf.union(i*n+j, (i+dx)*n+j+dy)
                        
        res = 0
        uf.clean()
        ans = 0
        groups = Counter()
        groups_count = Counter()
        for i,j in enumerate(uf.root):
            x1,y1 = i//n, i%n
            groups[j] += max(grid[x1][y1], 0)
            groups_count[j] += 1
            
        res = 0
        for i,j in groups.items():
            if j:
                res += (total-j)*groups_count[i]
                
        return res

        
        
        