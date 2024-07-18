class Disjoint:
    def __init__(self , n):
        self.root = [*range(n)]
        self.rank = [1] * n
        
    def find(self , x):
        if x == self.root[x]:
            return x
        x = self.root[x] = self.find(self.root[x])
        return x
    
    def union(self , vals):
        x , y = vals
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
        
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        if not pairs:
            return s
        
        n = len(s)
        graph = Disjoint(n)
        [*map(graph.union , pairs)]
            
        graph.clean()
        
        converted = defaultdict(lambda : [[],[]])
        for i in range(n):
            converted[graph.root[i]][0].append(i)
            converted[graph.root[i]][1].append(s[i])
            
        [*map(lambda arr : arr[1].sort() , converted.values())]
         
        res = [''] * n
        for i , j in converted.values():
            for index , letter in zip(i , j):
                res[index] = letter
                
        
        return ''.join(res)
        
            
        