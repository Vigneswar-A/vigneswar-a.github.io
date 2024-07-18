class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while (n := len(nums)) > 1:
            new_nums = [0] * (n//2)
            for i in range(n // 2):
                new_nums[i] = (max if i%2 else min)(nums[2*i] , nums[2*i + 1])
            nums = new_nums
                
        return nums[0]
                
        