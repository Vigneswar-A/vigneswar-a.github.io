class Solution:
    def totalNQueens(self, n: int) -> int:
        
        queenpos = []
        res = 0
        def backtrack(row=0):
            if row == n:
                nonlocal res
                res += 1

            for col in range(n):
                for qx, qy in queenpos:
                    if qx+qy == row+col or qx-qy == row-col or qx == row or qy == col:
                        break
                else:
                    queenpos.append((row, col))
                    backtrack(row+1)
                    queenpos.pop()
                    
        backtrack()
        
        return res
                    
                    
                
        