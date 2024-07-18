class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        
        distance = 0
        
        tx,ty = tree
        sx,sy = squirrel
        res = float('inf')
        
        for nx,ny in nuts:  
            distance += abs(tx-nx) + abs(ty-ny)
        
        for nx,ny in nuts:
            res = min(res , 2*distance - (abs(tx-nx) + abs(ty-ny)) + abs(sx-nx) + abs(sy-ny))
            
        return res
            
        
        