class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        
        prefix = list(accumulate(nums))
        n = len(nums)
        
        for j in range(3, n-3):
            hashset = set()
            for i in range(1, j-1):       
                if prefix[i-1] == prefix[j-1]-prefix[i]:
                    hashset.add(prefix[i-1])
            for k in range(j+2, n-1):
                if prefix[k-1]-prefix[j] == prefix[-1]-prefix[k] and prefix[k-1]-prefix[j] in hashset:
                    return True
        