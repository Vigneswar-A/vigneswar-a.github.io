class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        
        nums = deque(nums)
        min_val = min(nums)
        count = 0
        while nums[0] != min_val:
            count += 1
            nums.appendleft(nums.pop())
            
        if list(nums) != sorted(nums):
            return -1
        
        return count
        