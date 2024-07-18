
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]


    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def clean(self):
        for i in range(len(self.root)):
            self.find(i)
        return self.root
    
    
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        

        order = sorted(range(len(edges)), key=lambda i : edges[i][-1])
        edges.sort(key=lambda t:t[-1])
        
        def get_cost(to_delete=None, to_include=None):
            uf = UnionFind(n)
            total_cost = 0
            
            if to_include is not None:
                u,v,cost = edges[to_include]
                uf.union(u, v)
                total_cost += cost
                
            for i in range(len(edges)):
                if to_delete == i or to_include == i:
                    continue     
                u,v,cost = edges[i]
                if uf.union(u, v):
                    total_cost += cost
                    
            return total_cost if len(set(uf.clean())) == 1 else inf

        mst_cost = get_cost()
        pcrit = set()
        crit = set()

        for i in range(len(edges)):
            if get_cost(to_delete = i) > mst_cost:
                crit.add(order[i])
                
            if get_cost(to_include = i) == mst_cost:
                pcrit.add(order[i])
                

        return [crit, pcrit.difference(crit)]







        