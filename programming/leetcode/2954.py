class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        
        prefix = list(accumulate(nums)) + [0]
        counts = Counter()
        
        for  i in range(k):
            counts[nums[i]] += 1
            
        res = 0
        if len(counts) >= m:
            res = prefix[k-1]

        for i in range(len(nums)-k):
            counts[nums[i]] -= 1
            if counts[nums[i]] == 0:
                del counts[nums[i]]
                        
            counts[nums[i+k]] += 1
            
            if len(counts) >= m:
                res = max(res, prefix[i+k]-prefix[i])
            
        return res
            
        
            
        