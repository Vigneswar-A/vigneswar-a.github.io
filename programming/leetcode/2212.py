class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_index = 0
        max_index = 0
        
        for i, n in enumerate(nums):
            if n < nums[min_index]:
                min_index = i
            elif n > nums[max_index]:
                max_index = i

        return min(i + 2 - abs(min_index - max_index) , max(min_index , max_index) + 1 , i - min(min_index , max_index) + 1)