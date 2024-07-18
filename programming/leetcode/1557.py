class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hashmap = set()
        
        for i in range(len(s) - k + 1):
            hashmap.add(s[i:i+k])
            
        return len(hashmap) == 2**k
    
    
        