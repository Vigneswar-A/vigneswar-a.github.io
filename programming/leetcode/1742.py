class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        coordinates = sorted(x for x,y in points)
        res = 0
        for i in range(len(coordinates)-1):
            res = max(res, coordinates[i+1]-coordinates[i])
            
        return res
        