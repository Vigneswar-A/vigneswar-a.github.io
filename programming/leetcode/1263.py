class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        @cache
        def dp(dice=0, current_sum=0):
            if dice == n and current_sum == target:
                return 1
            
            elif dice == n or current_sum > target:
                return 0
            
            res = 0
            for face in range(1, k+1):
                res += dp(dice+1, current_sum + face)
                
            return res
        
        return dp()%1000000007
                
        