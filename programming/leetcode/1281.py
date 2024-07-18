class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s) 
        prefix = [[0]*26 for _ in range(n+1)]
        
        for i in range(len(s)):
            for j in range(26):
                prefix[i][j] += prefix[i-1][j]
            prefix[i][ord(s[i])-97] += 1
            
        res = []
        for l, r, c in queries:
            counts = [0]*26
            for i in range(26):
                counts[i] = prefix[r][i] - prefix[l-1][i]
            
            odds = 0
            for i in counts:
                if i%2:
                    odds += 1
            res.append(odds//2 <= c)
        
        return res
                