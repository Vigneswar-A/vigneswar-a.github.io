class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        
        
        
        def dp(nums):
            if len(nums) <= 1:
                return 1
            left = [i for i in nums if i < nums[0]]
            right = [i for i in nums if i > nums[0]]
            return (comb(len(left)+len(right), len(left))*dp(left)*dp(right))%(1000000007)
        
        return dp(nums)-1
        
        
        
        
                
                