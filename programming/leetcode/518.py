class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = defaultdict(lambda : 0 , {0:1})
        
        for coin in coins:
            for i in range(coin , amount + 1):       
                dp[i] += dp[i - coin]
                         
        return dp[amount]
                    
        