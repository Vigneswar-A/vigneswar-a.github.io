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
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        initial.sort()
        
        n = len(graph)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(n):          
                if graph[i][j]:
                    uf.union(i, j)

        def M(to_remove):
            count = 0
            for i in range(n):
                for infected in initial:
                    if infected == to_remove:
                        continue
                    if uf.is_connected(infected, i):
                        count += 1
                        break
            return count

        return min(initial, key=M)



                        
                        
                    
                    


            