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

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:

        edgeList.sort(key = lambda arr : arr[-1])
        order = sorted(range(len(queries)), key = lambda idx : queries[idx][-1])
        queries.sort(key = lambda arr : arr[-1])
        
        uf = UnionFind(n)

        res = [None] * len(queries)
        p = q = 0
        for idx, (i, j, cost) in enumerate(queries):
            while p < len(edgeList) and edgeList[p][-1] < cost:
                uf.union(edgeList[p][0], edgeList[p][1])
                p += 1
            res[order[idx]] = uf.is_connected(i, j)
        
        return res



