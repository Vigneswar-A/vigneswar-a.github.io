class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        mn = mx = res = nums[0]
        
        for i in nums[1:]:
            mn , mx = min(mx * i , i , mn * i) , max(mx * i , i , mn * i)
            res = max(mx , res)
            
        return res
        