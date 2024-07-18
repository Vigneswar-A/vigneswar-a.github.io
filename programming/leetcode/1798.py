class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        counts = Counter(nums)
        res = 0
        for i,c in counts.items():
            res += min(c, counts[k-i])
        return res//2
            
        