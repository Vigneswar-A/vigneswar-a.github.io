class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        
        counts = Counter(nums)
        
        pairs = left = 0
        for num,count in counts.items():
            pairs += count//2
            if count%2:
                left += 1
        
        return [pairs, left]
            
        