class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        currpt = 0
        indices = sorted(range(len(plantTime)), key=growTime.__getitem__, reverse = 1)
        res = 0
        
        for i in indices:
            currpt += plantTime[i]
            res = max(res, growTime[i]+currpt)
            
        return res
            
            
            
        