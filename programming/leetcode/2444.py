class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0]*(n+1)
        hashmap = {}
        
        for i in range(len(s)):
            
            for j in range(ord(s[i])-k, ord(s[i])+k+1):
                
                if chr(j) not in hashmap:
                    continue
                
                dp[i] = max(dp[i], dp[hashmap[chr(j)]]+1)
            hashmap[s[i]] = i
        
        return max(dp)+1
        