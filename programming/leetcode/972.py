class Solution:
    def knightDialer(self, n: int) -> int:

        dialpad = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [None,0,None]
        ]
        
        ways = {
            0 : [4, 6],
            1 : [6, 8],
            2 : [7, 9],
            3 : [4, 8],
            4 : [3, 9, 0],
            5 : [],
            6 : [1, 7, 0],
            7 : [2, 6],
            8 : [1, 3],
            9 : [2, 4]
            
        }
                        
        dp = [1]*10
        for _ in range(n-1):
            nxt = [0]*10
            for i in range(10):
                for j in ways[i]:
                    nxt[j] += dp[i]
            dp = nxt
            
        return sum(dp)%(10**9+7)
