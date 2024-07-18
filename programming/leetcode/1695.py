class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        sweepline = [0] * len(nums)
        
        for u,v in requests:
            sweepline[u] += 1
            if v+1 < len(nums):
                sweepline[v+1] -= 1
            
        priority = list(accumulate(sweepline))
        
        priority.sort(reverse=1)
        nums.sort(reverse=1)
        
        res = 0
        for i,j in zip(priority, nums):
            res += i*j
            
        return res%1000000007
            
        