class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexmap = {} #nums[index] -> index 
        
        for i , n in enumerate(nums):
            rem = target - n
            if rem in indexmap:
                return indexmap[rem] , i
            indexmap[n] = i
            
        
        