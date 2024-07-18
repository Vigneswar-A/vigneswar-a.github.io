class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        stack = []
        res = [-1]*n
        
        for i in range(2*n):
            while stack and nums[i%n] > nums[stack[-1]]:
                idx = stack.pop()
                res[idx%n] = nums[i%n]
            
            stack.append(i%n)
            
        return res
                
                