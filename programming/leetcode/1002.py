class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        
        stack = []
        res = 0
        
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
            left = 0
            right = len(stack)-1
            
            while left <= right:
                mid = left + right >> 1
                if nums[stack[mid]] <= nums[i]:
                    right = mid-1
                else:
                    left = mid+1
            res = max(res, i-stack[left])

            
        return res
                
                
            
        