class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        
        
        res = []
        prev = "-"
        count = 0
        for i,c in enumerate(s):
            if prev == c:
                count += 1
            else:
                if count >= 3:
                    res.append([i-count, i-1])
                prev = c
                count = 1
        
        return res + ([[i-count+1, i]] if count >= 3 else [])
            
                