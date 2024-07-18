class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        dp = [[0]*numCourses for _ in range(numCourses)]
        
        for u,v in prerequisites:
            dp[u][v] = 1
                   
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    dp[i][j] = max(dp[i][j], dp[i][k]&dp[k][j])
                    
        return [dp[i][j] for i,j in queries]
            
        
        