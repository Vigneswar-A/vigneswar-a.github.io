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

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind(m*n)
        graph = [[0]*n for _ in range(m)]

        def nei(x, y):
            for dx,dy in [(0,1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= x+dx < m and 0 <= y+dy < n and graph[x+dx][y+dy] == 1:
                    yield n*(x+dx) + (y+dy)

        res = []
        count = 0
        for x,y in positions:
            if graph[x][y] == 1:
                res.append(count)
                continue
            graph[x][y] = 1
            idx = n*x+y
            count += 1
            for nxt in nei(x, y):
                if uf.union(idx, nxt):
                    count -= 1
            res.append(count)

        return res