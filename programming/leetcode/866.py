class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        
        ax1, ay1, ax2, ay2 = rec1
        bx1, by1, bx2, by2 = rec2
        
        length = (min(ax2, bx2) - max(ax1, bx1))
        breadth = (min(ay2, by2) - max(ay1, by1))
        
        return length > 0 and breadth > 0