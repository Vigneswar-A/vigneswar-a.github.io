class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        nums = sorted(grid[i][j] for i in range(len(grid)) for j in range(len(grid[0])))
        n = len(nums)
        median = nums[n//2]
        
        res = 0
        for i in nums:
            q, r = divmod(abs(median-i), x)
            if r:
                return -1
            res += q
            
        return res
            