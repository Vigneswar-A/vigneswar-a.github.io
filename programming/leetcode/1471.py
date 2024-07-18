class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        
        m, n = len(seats), len(seats[0])
        
        @cache
        def dp(i=0, currmask=0, prevmask=0):
            if i == m:
                return 0
            
            res = 0
            for j in range(n):
                if seats[i][n-j-1] == '.'\
                and (~currmask&(1 << j)) \
                and (j == n-1 or ~prevmask&(1 << j+1))\
                and (j == 0 or ~prevmask&(1 << j-1))\
                and (j == n-1 or ~currmask&(1 << j+1))\
                and (j == 0 or ~currmask&(1 << j-1)):
                    res = max(res, dp(i, currmask|(1 << j), prevmask)+1)
                    
            return max(dp(i+1, 0, currmask), res)
                
        return dp()
                    