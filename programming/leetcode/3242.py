class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = [0]*101
        max_count = 0
        res = 0
        for i in nums:
            counts[i] += 1
            if counts[i] == max_count:
                res += max_count
            elif counts[i] > max_count:
                res = counts[i]
                max_count = counts[i]
                
        return res
            
            
        