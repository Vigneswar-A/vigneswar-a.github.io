class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        h = len(triangle)
        
        for i in range(1 , h):
            for j in range(i + 1):
                if 0 < j < i:
                    triangle[i][j] += min(triangle[i - 1][j - 1] , triangle[i - 1][j])
                elif j:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += triangle[i - 1][j]
        

        return min(triangle[-1])
                
                
        