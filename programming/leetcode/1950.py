class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        pos = True
        
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                pos = not pos
                
        return 1 if pos else -1
        
        