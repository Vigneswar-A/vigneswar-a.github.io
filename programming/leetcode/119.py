class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def next_row(row):
            res = [1]
            for i in range(len(row) - 1):
                res.append(row[i] + row[i + 1])
            res.append(1)
            return res
        
        row = [1]
        for _ in range(rowIndex):
            row = next_row(row)
            
        return row
        