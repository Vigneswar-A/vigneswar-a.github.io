class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = sorted(nums)
        
        while stack and stack[-1] == nums[-1]:
            stack.pop()
            nums.pop()
            
        while stack and stack[0] == nums[0]:
            stack.pop(0)
            nums.pop(0)
            
        return len(stack)
        