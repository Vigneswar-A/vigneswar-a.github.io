class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        hashmap = set(nums)
        res = -1
        for num in nums:
            if -num in nums:
                res = max(abs(num), res)
                
        return res
            
        