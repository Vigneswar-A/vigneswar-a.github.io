class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        squares = [i*i for i in range(1, int(sqrt(n))+1)]
        
        if n in squares:
            return True
        
        @cache
        def dp(num = 0, player = 1):
            if num == n:
              
                return not player
            
            ans = -inf if player else inf
            func = max if player else min
            for sq in squares:
                if num+sq <= n:
                    ans = func(dp(num+sq, not player), ans)
                    if ans == player:
                        return ans
            return ans
               

            
        
        return dp()
                    
        

            
        
        
        
        
        
        