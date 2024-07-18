class Solution:
    def minMovesToCaptureTheQueen(self, rx: int, ry: int, bx: int, by: int, qx: int, qy: int) -> int:
        # can rook kill queen directly?
        for dx,dy in [(0,1), (1,0), (-1,0), (0,-1)]:
            for d in range(8):
                if rx+dx*d == qx and ry+dy*d == qy:
                    return 1
                if rx+dx*d == bx and ry+dy*d == by:
                    break
        
        # can bishop kill queen by moving diagonally?
        for di in [1, -1]:
            for d in range(8):
                if bx+d*di == qx and by+d*di == qy:
                    return 1
                elif bx+d*di == rx and by+d*di == ry:
                    break
                    
            # anti diagonally
            for d in range(8):
                if bx+d*di == qx and by-d*di == qy:
                    return 1
                elif bx+d*di == rx and by-d*di == ry:
                    break
                    
        # It can be proved that we can kill in 2 moves at most
        return 2
      
            
            
        