class Solution:
    def minimumSplits(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        @cache
        def dp(idx=0):
            if idx == n:
                return 0
            

            prev = nums[idx]
            ans = inf
            for nxt in range(idx, n):

                if gcd(prev, nums[nxt]) == 1:
                    break
                prev = gcd(nums[nxt],prev)
                ans = min(ans, dp(nxt+1)+1)
            return ans
        
        return dp()
                
                    
                
        