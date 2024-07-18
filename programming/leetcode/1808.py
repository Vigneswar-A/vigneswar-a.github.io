class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        
        prefix = list(accumulate(stones)) + [0]
        n = len(stones)
        dp = [[0] * (n+1) for _ in range(n+1)]
        
        for right in range(n):
            for left in reversed(range(right)):
                left_score = prefix[right] - prefix[left]
                right_score = prefix[right-1] - prefix[left-1]
                dp[left][right] = max(left_score - dp[left+1][right], right_score - dp[left][right-1])

        return dp[0][n-1]
        
        