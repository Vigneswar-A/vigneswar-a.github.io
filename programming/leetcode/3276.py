class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = sorted(Counter(word).values(), reverse=1)
        res = 0
        
        for i,c in enumerate(counts, 0):
            res += (i//8+1)*c
            
        return res
           
        
            
        