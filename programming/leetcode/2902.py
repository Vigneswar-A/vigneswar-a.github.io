class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = -1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                n1, n2 = nums[i], nums[j]
                if max(map(int, str(n1))) == max(map(int, str(n2))):
                    res = max(res, n1+n2)
                    
        return res
                    
        