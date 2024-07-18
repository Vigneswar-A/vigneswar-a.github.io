class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        dp = [[0]*(k+1) for _ in range(n+1)]
        dp[0][0] = 1

        for a in range(1, n+1):
            prefix_sum = 0
            for b in range(k+1):
                prefix_sum = (prefix_sum + dp[a-1][b]) % MOD

                if b >= a:
                    prefix_sum = (prefix_sum - dp[a-1][b-a] + MOD) % MOD

                dp[a][b] = prefix_sum

        return dp[-1][-1]
        # @cache
        # def dp(n=n, k=k):
        #     if n == 0 and k == 0:
        #         return 1
        #     nonlocal count
        #     count += 1
        #     res = 0
        #     for j in range(min(n, k+1), 0, -1):
        #         res += dp(n-1, k-(j-1))
        #     return res%(10**9+7)
        # res = dp()
        # print(count)
        # return res
                