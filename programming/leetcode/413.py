class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        res = 0
        count = 0
        
        for i in range(1 , len(nums) - 1):
            if nums[i + 1] - nums[i] == nums[i] - nums[i - 1]:
                count += 1

            else:
                res += (count + 1) * (count) / 2
                count = 0
                
        return int(res + (count + 1) * (count) / 2)
                
                
                
                
        