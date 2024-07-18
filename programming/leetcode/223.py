class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        aarea = abs(ax2-ax1) * abs(ay2-ay1)
        barea = abs(bx2-bx1) * abs(by2-by1)
        
        y1 = max(ay1, by1)
        y2 = min(ay2, by2)
        x1 = max(ax1, bx1)
        x2 = min(ax2, bx2)

        area = 0
        if x2 > x1 and y2 > y1:
            area = (x2-x1) * (y2-y1)
        
        return aarea + barea - area