class UnionFind:
    def __init__(self , n):
        self.root = [*range(n)]
        self.rank = [1] * n
        
    def find(self , x):
        if x == self.root[x]:
            return x
        x = self.root[x] = self.find(self.root[x])
        return x
    
    def union(self , x, y):
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
            if self.root[i] != i:
                self.root[i] = self.find(i)
        return self.root

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        def similar(s1, s2):
            idx1 = None
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    if idx1 is None:
                        idx1 = i
                    elif s1[i] == s2[idx1] and s1[idx1] == s2[i]:
                        return s1[i+1:] == s2[i+1:]
                    else:
                        return False
            return idx1 is None

                    
        n = len(strs)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i+1, n):
                if similar(strs[i], strs[j]):
                    print(i, j)
                    uf.union(i, j)

        return len(set(uf.clean()))
