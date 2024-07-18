class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        
        
        @lru_cache(1000)
        def dp(i=0, heads=0):
            if i == len(prob):
                return heads == target
            
            return dp(i+1, heads+1)*prob[i] + dp(i+1, heads)*(1-prob[i])
        
        return dp()