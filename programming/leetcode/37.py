class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        row_nums = [set() for _ in range(9)]
        col_nums = [set() for _ in range(9)]
        box_nums = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row_nums[i].add(board[i][j])
                    col_nums[j].add(board[i][j])
                    box_nums[(i//3 * 3) + j//3].add(board[i][j])
                    

        filled = False
        def backtrack(row=0, col=0):
            nonlocal filled
            if filled:
                return
            
            if row == 9:
                filled = True
                return 
            
            if board[row][col] != '.':
                backtrack(row, col+1) if col != 8 else backtrack(row+1, 0)
                return 
            
            for i in range(1,10):
                n = str(i)
                box_idx = (row//3 * 3) + col//3
                if n in row_nums[row] or n in col_nums[col] or n in box_nums[box_idx]:
                    continue
                    
                board[row][col] = n
                row_nums[row].add(n)
                col_nums[col].add(n)
                box_nums[box_idx].add(n)
                
                backtrack(row, col+1) if col != 8 else backtrack(row+1, 0)
                
                if not filled:
                    board[row][col] = '.'
                    row_nums[row].discard(n)
                    col_nums[col].discard(n)
                    box_nums[box_idx].discard(n)

        backtrack()
                
            

            
                
        
        
                    

                    
                
                            
                                
                    
            