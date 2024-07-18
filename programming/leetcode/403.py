class Solution:
    def canCross(self, stones: List[int]) -> bool:   
        end = stones[-1]
        stones = set(stones)
        
        @cache
        def dp(x, k):
            if x == end:
                return True
            res = inf
            for step in {k+1, k, k-1}:
                if step and x+step in stones and dp(x+step, step):
                    return True
            
        
        return dp(0, 0)
            