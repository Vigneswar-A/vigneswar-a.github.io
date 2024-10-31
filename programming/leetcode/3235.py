class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        # floyd warshall implementation
        dp = [[inf]*26 for _ in range(26)]
        for u,v,c in zip(original, changed, cost):
            dp[ord(u)-ord('a')][ord(v)-ord('a')] = min(c, dp[ord(u)-ord('a')][ord(v)-ord('a')])
            
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dp[i][j] = min(dp[i][k]+dp[k][j], dp[i][j])
              
        # find cost
        res = 0
        for u,v in zip(source, target):
            if u != v:
                res += dp[ord(u)-ord('a')][ord(v)-ord('a')]
                
        return res if res != inf else -1
        
# "abadcdadac"
# "baddbccdac"
# ["d","c","d","c","b","a"]
# ["b","b","c","a","d","d"]
# [8,5,9,1,10,2]
        