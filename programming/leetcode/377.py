class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @cache
        def backtrack(total=0):
            if total == target:
                return 1
            
            if total > target:
                return 0
            
            count = 0
            for i in nums:
                count += backtrack(total+i)
                
            return count
        
        
        count = backtrack()
        return count
            
        