class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n,m = len(word1),len(word2)
        
        @cache
        def dp(i=0, j=0):
            if j == m:
                return (n-i)
            if i == n:
                return (m-j)
            if word1[i] != word2[j]:
                return 1+min(dp(i+1, j), dp(i+1, j+1), dp(i, j+1))
            return dp(i+1, j+1)
        
        return dp()
        