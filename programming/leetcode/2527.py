class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        min_pos = -1
        max_pos = -1
        invalid_pos = -1
        res = 0
        
        for i in range(len(nums)):
            if nums[i] > maxK or nums[i] < minK:
                invalid_pos = i
                
            if nums[i] == maxK:
                max_pos = i
                
            if nums[i] == minK:
                min_pos = i
                
            score = min(min_pos, max_pos) - invalid_pos
            if score > 0:
                res += score
                
        return res
                
                