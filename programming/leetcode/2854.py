class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        n = len(words)
        
        @cache
        def dp(c, i):
            if i == n:
                return 0
            ans1 = dp(c[0]+words[i][-1], i+1) + len(words[i])-(c[-1] == words[i][0])
            ans2 = dp(words[i][0] + c[-1], i+1) + len(words[i])-(c[0] == words[i][-1])
            return min(ans1, ans2)
        
        return dp(words[0][0]+words[0][-1], 1) + len(words[0]) 
            
            
            
        
        
        
        
        
        
        