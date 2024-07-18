class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        #finding sum of smallest in subarrays
        stack = []
        min_sum = 0
        for right in range(n+1):
            while stack and ((right == n) or (nums[right] <= nums[stack[-1]])):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                min_sum += (mid-left)*(right-mid)*nums[mid]
            stack.append(right)
            
        #finding sum of largest in subarrays
        stack = []
        max_sum = 0
        for right in range(n+1):
            while stack and ((right == n) or (nums[right] >= nums[stack[-1]])):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                max_sum += (mid-left)*(right-mid)*nums[mid]
            stack.append(right)
            
        return max_sum - min_sum
                