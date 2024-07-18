class Solution:
    def maxA(self, n: int) -> int:
 
        @cache
        def dp(moves=0, buffer=1, onscreen=0):
            if moves == n:
                return onscreen
            
            if moves>n:
                return 0
            
            return max(
                dp(moves+2, onscreen, onscreen), #select and copy
                dp(moves+1, buffer, onscreen+buffer) #paste
            )
        
        return dp()