class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        
        @cache
        def dp(i=0, even=True):
            if i == len(nums) and even:
                return 0
            elif i == len(nums):
                return -inf
            return max(dp(i+1, even)+nums[i], dp(i+1, not even)+(nums[i]^k))
        
        return dp()
            
                    
                
            
            