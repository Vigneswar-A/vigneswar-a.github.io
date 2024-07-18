class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        digitsum = defaultdict(list)
        
        for i,j in enumerate(nums):
            heappush(digitsum[sum(map(int, str(j)))], -j)
            
        res = -1
        for val in digitsum.values():
            if len(val) > 1:
                u = heappop(val)
                v = heappop(val)
                res = max(res, -u-v)
                
        return res
            
            
        