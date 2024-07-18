class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        dp = [[0]*(n+1) for _ in range(n+1)]
        longest = ""
        
        for i in range(n-1, -1, -1):
            for j in range(n):
                if i == j:
                    dp[i][j] = 1
                    
                elif s[i] == s[j]:
                    dp[i][j] = i+1 == j or dp[i+1][j-1]
                
                if dp[i][j] and j-i+1 > len(longest):
                    longest = s[i:j+1]
                    
        return longest
                    
        