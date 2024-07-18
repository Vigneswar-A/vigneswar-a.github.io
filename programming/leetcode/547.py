class disjoint:
    def __init__(self , size):
        self.root = [*range(size)]
        
    def find(self , x):
        return self.root[x]
    
    def union(self , x , y):
        rootx = self.find(x)
        rooty = self.find(y)
        
        if rootx == rooty:
            return
        
        for i in range(len(self.root)):
            if self.root[i] == rooty:
                self.root[i] = rootx
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = disjoint(size := len(isConnected))
        for i in range(size):
            for j in range(size):
                if isConnected[i][j]:
                    graph.union(i , j)
        return len(set(graph.root))
        
                
                
                
                