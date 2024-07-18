memo =[[[1, 1, 1, 0], [0, 0, 0, 0]]] + [[[0, 0, 0, 0] for _ in range(2)] for _ in range(100000+1)]
class Solution:
    def checkRecord(self, n: int) -> int:
        
        MOD = (10**9+7)
        # states:
        # absent ever before
        # present absent late-1 late2  
        for i in range(1, n):
            # never absent before
            memo[i][0][0] = (memo[i-1][0][0]+memo[i-1][0][2]+memo[i-1][0][3])%MOD # present
            memo[i][0][1] = (memo[i-1][0][0]+memo[i-1][0][2]+memo[i-1][0][3])%MOD # absent
            memo[i][0][2] = memo[i-1][0][0] # late 1
            memo[i][0][3] = memo[i-1][0][2] # late 2
            
            # absent before
            memo[i][1][0] = (memo[i-1][1][0]+memo[i-1][1][2]+memo[i-1][1][3]+memo[i-1][0][1])%MOD # present
            memo[i][1][2] = (memo[i-1][1][0]+memo[i-1][0][1])%MOD  # late 1
            memo[i][1][3] = memo[i-1][1][2] # late 2

        return sum(memo[n-1][0]+memo[n-1][1])%MOD
            

        