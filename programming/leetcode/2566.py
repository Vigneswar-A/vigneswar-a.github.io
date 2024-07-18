class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if len({nums[i], nums[j], nums[k]}) == 3:
                        res += 1
                        
        return res