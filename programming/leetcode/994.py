class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        
        for i in range(n%14 or 14):
            cells = [0]+[int(not (cells[i-1]^cells[i+1])) for i in range(1, len(cells)-1)]+[0]
            
            
        return cells