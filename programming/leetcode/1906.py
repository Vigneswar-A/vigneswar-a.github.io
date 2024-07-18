class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(k=1, bitmask=0):
            ans = 0
            for i in range(n):
                if bitmask&(1<<i):
                    continue
                for j in range(i+1, n):
                    if bitmask&(1<<j):
                        continue
                    score = gcd(nums[i], nums[j])*k
                    ans = max(ans, dp(k+1, bitmask|(1<<i)|(1<<j))+score)
                    
            return ans
                    
        return dp()
            
                        
      
                        
                        
                    
        