class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        
        prefix = list(accumulate(nums)) + [0]
        
        def get_sum(l, r=len(nums)-1): # get sum of nums[l:r+1]
            return prefix[r] - prefix[l-1]
        
        # 0 - i, i+1 - j, j+1 - n
        ids = [*range(len(nums)-1)]
        ans = 0
        for i in range(len(nums)):
            left_bound = bisect.bisect_left(ids, 1, lo=i+1, key = lambda j : get_sum(0, i) <= get_sum(i+1, j))
            right_bound = bisect.bisect_left(ids, 1, key = lambda j : get_sum(i+1, j) > get_sum(j+1))-1
            
            if left_bound == i or left_bound == len(nums) or right_bound == i or right_bound == len(nums):
                continue

            ans += max(right_bound - left_bound + 1, 0)
        
        return ans%(10**9 + 7)
            
                
                
        
        