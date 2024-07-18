class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        
        res = 0
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 1:
                for j in range(i, len(nums), 2):
                    if nums[j] == nums[i] and j+1<len(nums) and nums[j+1] == nums[i+1]:
                        
                        res = max(res, j-i+2)
                    elif nums[j] == nums[i]:
                        res = max(res, j-i+1)
                        break
                    else:
                        break
        return res or -1
                       
                    
        