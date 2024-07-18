class Solution:
    def canJump(self, nums: List[int]) -> bool:

        farthest = 0
        currstop = nums[0]
        for i in range(len(nums)):
            if i > currstop:
                break

            farthest = max(i+nums[i], farthest)
            
            if i == currstop:
                currstop = farthest
                farthest = 0
            

        return currstop >= len(nums)-1



