class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currmax = maxsum = -float('inf')    
        currmin = minsum = float('inf')
        sum_ = 0
        for i in nums:            
            maxsum = max((currmax := max(currmax + i , i)) , maxsum)
            minsum = min((currmin := min(currmin + i , i)) , minsum)
            sum_ += i
        
        return max(maxsum , (sum_ - minsum) if minsum != sum_ else sum_)
        