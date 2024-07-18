class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort(reverse=1)
        left = 0
        ans = 0
        for right in range(len(nums)):
            
            k -= nums[left] - nums[right]
            while left < right and k < 0:
                left += 1
                k += (right-left+1)*(nums[left-1]-nums[left])
            ans = max(ans, right-left+1)
                
        return ans
            
                
                
            
        