class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        
        count = 0
        streak = 1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                streak += 1
                
            else:
                count += ((streak)*(streak+1))//2
                streak = 1
                
        return count + ((streak)*(streak+1))//2
            