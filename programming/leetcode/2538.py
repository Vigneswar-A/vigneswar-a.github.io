class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        @cache
        def get_cost(target):
            res = 0
            for i in range(len(nums)):
                res += abs(target-nums[i])*cost[i]

            return res
        
        right = max(nums)
        left = 0
        
        while left+1 < right:
            mid = left+right >> 1
            if get_cost(mid-1) > get_cost(mid) < get_cost(mid+1):
                return get_cost(mid)
            elif get_cost(mid-1) > get_cost(mid):
                left = mid
            else:
                right = mid

        return min(get_cost(left), get_cost(right), get_cost(mid))