class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @cache
        def dp(i=0, j=0):
            if i == len(word1) or j == len(word2):
                return 0
            if word1[i] == word2[j]:
                return 1+dp(i+1, j+1)
            
            return max(dp(i+1, j), dp(i, j+1))
        
        return len(word1) + len(word2) - 2*dp()
        
        