class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = ((0,1) , (1,0) , (0,-1) , (-1,0))
        obstacles = set(map(tuple , obstacles))
        
        d = 0
        x,y = (0,0)
        max_dist = 0
        for command in commands:
            if command > 0:
                for move in range(command):
                    dx,dy = directions[d]
                    if (x+dx , y+dy) not in obstacles:
                        x += dx
                        y += dy
                    else:
                        break
                    
            else:
                if d == 0 and command == -2:
                    d = 3
                elif d == 3 and command == -1:
                    d = 0
                else:
                    d += (1 if command == -1 else -1)
                    
            max_dist = max(x**2 + y**2 , max_dist)
         
        return max_dist
        