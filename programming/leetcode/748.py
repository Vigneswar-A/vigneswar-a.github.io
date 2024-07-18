class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        index_map = {j:i for i,j in enumerate(nums)}
        nums.sort(reverse = 1)
        
        if nums[0] >= 2 * nums[1]:
            return index_map[nums[0]]
        
        return -1
                
        