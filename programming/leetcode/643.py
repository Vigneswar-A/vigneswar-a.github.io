class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:        
        max_sum = currsum = sum(nums[:k])
        
        for i in range(k, len(nums)):
            currsum = currsum - nums[i-k] + nums[i]
            max_sum =  max(currsum, max_sum)
        
        return max(currsum, max_sum)/k
            
            
            
        
        