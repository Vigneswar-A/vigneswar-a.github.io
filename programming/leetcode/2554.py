class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        
        robot.sort()
        factory.sort()
        
        @cache
        def dp(i, j):
            if i == len(robot):
                return 0
            elif j == len(factory):
                return inf
            
            dist = 0
            res = dp(i, j+1) # skip this factory
            
            # number of robots to assign for factory j
            for k in range(i, len(robot)):
                if k-i >= factory[j][1]: # if number of robots greater than limit
                    break
                dist += abs(factory[j][0]-robot[k])
                res = min(res, dist+dp(k+1, j+1))
            return res
        
        return dp(0, 0)
                
        