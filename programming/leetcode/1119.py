class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        x,y = (0,0)
        dx,dy = (1,0)
        clockwise = {(1,0):(0,1), (0,1):(-1,0), (-1,0):(0,-1), (0,-1):(1,0)}
        anticlockwise = {(1,0):(0,-1), (0,-1):(-1,0), (-1,0):(0,1), (0,1):(1,0)}
        
        for move in instructions:
            if move == 'G':
                x += dx
                y += dy
                
            elif move == 'L':
                dx,dy = clockwise[(dx,dy)]
                
            else:
                dx,dy = anticlockwise[(dx,dy)]
                
        return (x,y) == (0,0) or (dx,dy) != (1,0)
                
            
                
            
                
            
        