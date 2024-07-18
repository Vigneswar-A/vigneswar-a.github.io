class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        
        n = len(obstacles)
        
        res = [1]
        sub = [obstacles[0]]
        for i in range(1, n):
            if sub[-1] <= obstacles[i]:
                sub.append(obstacles[i])
                res.append(len(sub))
            else:
                j = bisect.bisect(sub, obstacles[i])
                res.append(j+1)
                sub[j] = obstacles[i]

        return res      
        