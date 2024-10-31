class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        ans = k*(k+1)//2
        j = k+1
        for i in nums:
            while j in nums:
                j += 1
            if i <= k:
                
                ans = ans - i + j
                j += 1
                
        return ans
        