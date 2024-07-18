class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        get_slope = lambda x1 , y1 , x2 , y2 : ((y2 - y1) / (x2 - x1)) if x1 != x2 else float('inf')
        
        ref = coordinates[0]
        slope = get_slope(*ref , *coordinates[1])
        
        for point in coordinates[2:]:
            if get_slope(*ref , *point) != slope:
                return False
            
        return True
            