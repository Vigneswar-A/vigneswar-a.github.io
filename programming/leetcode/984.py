class UnionFind:
    def __init__(self , n):
        self.root = [*range(n)]
        self.rank = [1] * n
        
    def find(self , x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self , x , y):
        rootx = self.find(x)
        rooty = self.find(y)
        
        if rootx == rooty:
            return False
        
        if self.rank[rootx] > self.rank[rooty]:
            self.root[rooty] = rootx
        elif self.rank[rooty] > self.rank[rootx]:
            self.root[rootx] = rooty
        else:
            self.rank[rootx] += 1
            self.root[rooty] = rootx
            
        return True
        
    def clean(self):
        for i in range(len(self.root)):
            if self.root[i] != self.root[self.root[i]]:
                self.find(i)
    
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = UnionFind(len(stones))
        
        for i in range(len(stones)):
            for j in range(i+1,len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph.union(i,j)     
        
        graph.clean() 
        return len(stones) - len(set(graph.root))
        
        