class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        n = len(nums)
        
        for last in range(n-1,-1,-1):
            if nums[last]:
                break
        else:
            return 0
        
        res = 1
        prev = inf
        for i in range(last+1):
            if nums[i]:
                res *= max(i-prev, 1)
                res %= 1000000007
                prev = i

        
        return res
            
                
        