class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        
        max_sq = 0
        res = 0
        for l,b in rectangles:
            sq = min(l, b)
            if sq > max_sq:
                res = 1
                max_sq = sq
            elif sq == max_sq:
                res += 1
                
        return res
        