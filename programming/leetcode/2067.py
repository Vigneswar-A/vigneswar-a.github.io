class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        m = len(points[0])
        prev = [0]*m 
        
        for i in range(n):
            curr = [0]*(m+1)
            max_so_far = 0
            for j in range(m):
                max_so_far = max(max_so_far-1, prev[j])
                curr[j] = max(curr[j], points[i][j]+max_so_far)
                
                
            max_so_far = 0
            for j in range(m-1,-1,-1):
                max_so_far = max(max_so_far-1, prev[j])
                curr[j] = max(curr[j], points[i][j]+max_so_far)
            prev = curr
        return max(prev)
    
                    