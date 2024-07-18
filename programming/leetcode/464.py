class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        if desiredTotal == 0: #edge condition game ends before starting
            return True
        
        if maxChoosableInteger*(maxChoosableInteger+1) >> 1 < desiredTotal:
            return False
        
        @cache
        def dp(bitmask = 0):
            to_play, is_max, total = [], True, 0
            
            for i in range(1, maxChoosableInteger+1):
                if bitmask&(1 << i) == 0:
                    to_play.append(i)
                else:
                    total += i
                    is_max = not is_max
      
            if total >= desiredTotal:
                return not is_max
            
            for i in to_play:
                if dp(bitmask|(1 << i)) == is_max:
                      return is_max
            
            return not is_max
        
        ans = dp()
        dp.cache_clear()
        return ans > 0