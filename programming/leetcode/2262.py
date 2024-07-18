class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        n = len(questions)
        dp = Counter()
        ans = 0
        for i in range(n-1,-1,-1):
            dp[i] = max(dp[i+1], dp[i+questions[i][1]+1] + questions[i][0])
            if dp[i] > ans:
                ans = dp[i]
            
        return ans
        