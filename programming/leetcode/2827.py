class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True 
        
        factors = defaultdict(set)
        uf = UnionFind(max(nums)+1)
        
        for i in nums:
            if i == 1:
                return False
            for j in range(2, isqrt(i)+1):
                if i%j == 0:
                    uf.union(i, j)
                    uf.union(i, i//j)
            
        root = None
        for i in nums:
            if root is None:
                root = uf.find(i)
            elif root != uf.find(i):
                return False
            
        return True
    
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
            return False
        
        if self.rank[rootx] > self.rank[rooty]:
            self.root[rooty] = rootx
        elif self.rank[rootx] < self.rank[rooty]:
            self.root[rootx] = rooty
        else:
            self.rank[rootx] += 1
            self.root[rooty] = rootx
        return True
    
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
            
        
        
        
        
        
        
        
        
        