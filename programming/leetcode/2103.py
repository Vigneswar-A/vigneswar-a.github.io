class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def find_bound(x, y):
            i, j = x, y
            while i+1 < len(land) and land[i+1][j]:
                i += 1
            while j+1 < len(land[0]) and land[i][j+1]:
                j += 1
            return (x, y, i, j)
        
        res = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 0 or (i and land[i-1][j]) or (j and land[i][j-1]):
                    continue
                res.append(find_bound(i, j))

        return res
    
        
        
        