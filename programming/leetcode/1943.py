class Solution:
    def countQuadruples(self, firstString: str, secondString: str) -> int:
        
        hashmap1 = {}
        hashmap2 = {}
        
        for i,c in enumerate(firstString):
            if c not in hashmap1:
                hashmap1[c] = i
            
        for i,c in enumerate(secondString):
            hashmap2[c] = i

        get_val = lambda c: hashmap1.get(c, inf) - hashmap2.get(c, -inf)
        
        min_val = min(map(get_val, ascii_lowercase))
        
        return sum(1 for c in ascii_lowercase if get_val(c) == min_val) if min_val != inf else 0
            
            
        