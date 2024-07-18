class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        
        n = len(nums)
        stack = []
        res = 0
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                j = stack.pop()
                res += i-j
            stack.append(i)
            
        return  res + sum(n-i for i in stack)