class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                box_id = i//3 + (j//3)*3
                n = board[i][j]
                if n == '.':
                    continue
                if n in row[i] or n in col[j] or n in box[box_id]:

                    return False
                
                row[i].add(n)
                col[j].add(n)
                box[box_id].add(n)
        return True