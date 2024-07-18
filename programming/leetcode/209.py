class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l , r = 0 , 1
        size = len(nums)
        total = nums[0]
        res = float('inf')
        
        while l < size:        
            if total >= target:
                res = min(res , r - l)
                total -= nums[l]
                l += 1
            
            elif r < size and total < target:
                total += nums[r]
                r += 1
                
            else:
                total -= nums[l]
                l += 1
            
        
        return res if res != float('inf') else 0
        
                
        
            
        