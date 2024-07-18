class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        left = 0
        right = len(nums) - 1
        add = partial(res.insert , 0)
        
        while left <= right:
            if -nums[left] > nums[right]:
                add(nums[left] ** 2)
                left += 1
            else:
                add(nums[right] ** 2)
                right -= 1
                
        return res
        