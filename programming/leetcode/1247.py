class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        
        even = odd = 0
        for i in range(len(nums)):
            bound = min(nums[i-1] if i else inf, nums[i+1] if i+1 < len(nums) else inf) - 1
            if bound <= nums[i]:
                if i%2:
                    even += nums[i] - bound
                else:
                    odd += nums[i] - bound
                    
        return min(odd, even)
            
        
                    
                
        