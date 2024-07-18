class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        
        prefix = list(accumulate(nums)) + [0]
        n = len(nums)
        res = []
        for i in range(n):
            if i >= k and i + k < n:
                res.append((prefix[i+k]-prefix[i-k-1])//(2*k+1))
            else:
                res.append(-1)
                
        return res
        