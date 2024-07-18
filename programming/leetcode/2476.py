class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        
        hashmap = defaultdict(list)
        
        for i,c in enumerate(s):
            hashmap[c].append(i)
            
        for i in range(26):
            c = chr(i+97)
            
            if c in hashmap and abs(int.__sub__(*hashmap[c]))-1 != distance[i]:
                return False
            
        return True
                
        