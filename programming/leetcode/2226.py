from collections import defaultdict
class Solution:
    def countPoints(self, rings: str) -> int:
        
        container=defaultdict(set)
        
        for i in range(len(rings)-1,-1,-2):
            container[rings[i]].add(rings[i-1])
        
        return tuple(container.values()).count({'R','G','B'})
                
            
        
            
        