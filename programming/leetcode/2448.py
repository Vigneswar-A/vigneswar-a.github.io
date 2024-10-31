class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        counts = Counter()
        for i in range(len(nums)):
            counts[i-nums[i]] += 1
        
        res = 0
        for v in counts.values():
            res += comb(v, 2)
            
        return comb(len(nums), 2)-res
        
       
        