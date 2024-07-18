class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        @cache
        def minimax(idx = 0, ismax = True):
            if idx == len(stoneValue):
                return 0
            
            best_score = -inf if ismax else inf
            maximise = max if ismax else min
            curr_score = 0
            
            for i in range(idx, min(idx+3, len(stoneValue))):
                curr_score += (stoneValue[i] if ismax else -stoneValue[i])
                best_score = maximise(best_score, minimax(i+1, not ismax) + curr_score)
                
            return best_score
        
        alice_score = minimax()
        minimax.cache_clear()

        if alice_score > 0:
            return "Alice"
        elif alice_score < 0:
            return "Bob"
        else:
            return "Tie"
            
            

            