class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        @cache
        def dp(x=startRow, y=startColumn, moves=0):
            if moves > maxMove:
                return 0
            
            if x < 0 or x == m or y < 0 or y == n:
                return 1
            
            return ( dp(x+1, y, moves+1)
                    +dp(x-1, y, moves+1)
                    +dp(x, y+1, moves+1) 
                    +dp(x, y-1, moves+1) )
        
        return dp()%1000000007
        