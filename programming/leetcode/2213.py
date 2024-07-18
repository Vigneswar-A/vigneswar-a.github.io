class UnionFind:
    def __init__(self, n):
        self.rank = [0]*n
        self.root = [*range(n)]
        
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
            
        elif self.rank[rootx] < self.rank[rooty]:
            self.root[rootx] = rooty
        
        else:
            self.rank[rootx] += 1
            self.root[rooty] = rootx
            
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
        
    def reset(self, x):
        self.root[x] = x
        self.rank[x] = 0
    
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        times = defaultdict(list)
        
        knows = {0, firstPerson}
        
        for u,v,time in meetings:
            times[time].append((u, v))
            
        uf = UnionFind(n)
        uf.union(0, firstPerson)
        
        for time, meeting in sorted(times.items()):     
            for u,v in meeting:
                uf.union(u, v)

            for u,v in meeting:
                if uf.is_connected(0, u):
                    knows.add(u)
                else:
                    uf.reset(u)
                if uf.is_connected(0, v):
                    knows.add(v)
                else:
                    uf.reset(v)
                           
        return knows
                
            
            
        
        
        