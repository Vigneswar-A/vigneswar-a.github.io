class UnionFind:
    def __init__(self, n):
        self.n = n
        self.root = [*range(n)]
        self.rank = [1]*n

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

        if self.rank[rootx] > rooty:
            self.root[rooty] = rootx

        elif self.rank[rooty] > rootx:
            self.root[rootx] = rooty

        else:
            self.rank[rootx] += 1
            self.root[rooty] = rootx

    def clean(self):
        for i in range(self.n):
            self.root[i] = self.find(i)
        return set(self.root)

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        edges.sort(reverse=1)
        uf1 = UnionFind(n)
        uf2 = UnionFind(n)

        count = 0
        for type,u,v in edges:
            u -= 1
            v -= 1
            if (type == 1) and uf1.union(u,v):
                count += 1
            if (type == 2) and uf2.union(u,v):
                count += 1
            if (type == 3):
                if uf1.connected(u,v) and uf2.connected(u,v):
                    count += 1
                uf1.union(u,v)
                uf2.union(u,v)

        return count if (len(uf1.clean()) == 1 and len(uf2.clean()) == 1) else -1
            