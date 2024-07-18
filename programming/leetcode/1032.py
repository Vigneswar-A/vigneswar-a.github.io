class UnionFind:
    def __init__(self, n):
        self.root = [*range(n)]
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
        
    def union(self, x, y):
        rootx = self.find(self.root[x])
        rooty = self.find(self.root[y])
        
        if rootx == rooty:
            return
        
        self.root[rootx] = rooty
        
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equations.sort(key = lambda s: s[1] == '!')
        graph = UnionFind(26)
        for equation in equations:
            if equation[1] == '=':
                graph.union(ord(equation[0])-97, ord(equation[-1])-97)
            elif graph.find(ord(equation[0])-97) == graph.find(ord(equation[-1])-97):
                return False
        return True
                
        
        
        