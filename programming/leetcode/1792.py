class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i] and k-(len(stack)) < n-i:
                stack.pop()
            stack.append(i)
            
        return [nums[i] for i in stack][:k]
        