class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        
        mask = (2**len(nums))-1
        
        @cache
        def dp(prev=None, bitmask=0):
            if bitmask == mask:
                return 1
            res = 0
            for i,num in enumerate(nums):
                if (1 << i)&bitmask or (prev is not None and num%prev and prev%num):
                    continue
                res += dp(num, bitmask|(1 << i))
            return res%(10**9 + 7)
        
        return dp()
                
            
            