class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        
        
        @cache
        def backtrack(idx=0, weight=0):
            if idx == len(stones):
                return abs(weight)
            
            return min(backtrack(idx+1, weight+stones[idx]), backtrack(idx+1, weight-stones[idx]))
            
        return backtrack()            
            