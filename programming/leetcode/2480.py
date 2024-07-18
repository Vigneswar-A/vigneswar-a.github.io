class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        
        sums = set()
        for i in range(len(nums)-1):
            currsum = nums[i]+nums[i+1]
            if currsum in sums:
                return True
            sums.add(currsum)
            
        return False