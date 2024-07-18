# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        
        def revert():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        visited = set()
        def backtrack(x=0, y=0, d=0):
            robot.clean()
            visited.add((x, y))
            
            for i in range(4):
                dx, dy = directions[(i+d)%4]
                if (x+dx, y+dy) not in visited and robot.move():
                    backtrack(x+dx, y+dy, (i+d)%4)
                    revert()
                
                robot.turnRight()

        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        backtrack()
                
            
        