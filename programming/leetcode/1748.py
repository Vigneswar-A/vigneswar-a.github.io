class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        
        players = sorted(zip(ages, scores))
        n = len(scores)

        dp = [[0]*(n+1) for _ in range(n+1)]
        
        for idx in range(n-1,-1,-1):
            for prev_idx in range(n-1,-2,-1):
                if prev_idx != -1 and players[idx][1] < players[prev_idx][1]:
                    dp[idx][prev_idx] = dp[idx+1][prev_idx]
                else:
                    dp[idx][prev_idx] = max(dp[idx+1][idx] + players[idx][1], dp[idx+1][prev_idx])
        return dp[0][-1]
                

        
        