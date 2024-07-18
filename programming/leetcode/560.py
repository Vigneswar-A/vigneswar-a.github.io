class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0]+list(accumulate(nums))
        res = 0
        counts = Counter()
        for i in prefix:
            res += counts[i-k]
            counts[i] += 1
            
            
        return res
            
                
                