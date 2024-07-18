class Disjoint:
    def __init__(self):
        self.root = {c : c for c in ascii_lowercase} #Map to store the translations
    
    def union(self , u , v):
        x , y = sorted([self.root[u] , self.root[v]]) #Root should be the minimum lexicographic letter
        
        if x == y:
            return False
        
        for c in ascii_lowercase: #Join the two elements
            if self.root[c] == y:
                self.root[c] = x

        
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        mapping = Disjoint() 
        
        for u , v in zip(s1 , s2):
            mapping.union(u , v) #Join the letters
            
        return ''.join(map(mapping.root.get , baseStr)) 