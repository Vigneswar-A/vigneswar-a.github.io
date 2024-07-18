class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        prev = nums[0]
        max_sum = currsum = prev
        
        for num in nums[1:]:
            if num > prev:
                currsum += num
                
            else:
                max_sum = max(max_sum, currsum)
                currsum = num
            
            prev = num
        
        return max(max_sum, currsum)
                