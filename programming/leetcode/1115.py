class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        def slope(x1,y1,x2,y2):
            return (y2-y1)/(x2-x1) if x2-x1 else float('inf')
        
        return len(set([slope(*points[0],*points[1]),slope(*points[1],*points[2]),slope(*points[0],*points[2])]))==3
        
        