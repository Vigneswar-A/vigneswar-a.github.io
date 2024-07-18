class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums: return 0
        maxseq = 0

        streak = 1
        for i in range(1, len(nums)):         
            if nums[i - 1] + 1 ==  nums[i]:
                streak += 1
                
            elif nums[i - 1] != nums[i]:
                maxseq = max(maxseq , streak)
                streak = 1
                
        return max(maxseq , streak)
                
            
                
        