class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        m,n = len(heights),len(heights[0])
        heap = [(0,0,0)]
        min_effort = [[inf]*n for _ in range(m)]
        min_effort[0][0] = 0
        while heap:
            effort, i, j = heappop(heap)
            heights[i][j] = -heights[i][j]
            for di, dj in [(0,1), (-1,0), (0,-1), (1,0)]:
                if 0 <= i+di < m and 0 <= j+dj < n and heights[i+di][j+dj] > 0 and min_effort[i+di][j+dj] > (max_diff := max(effort, abs(heights[i][j]+heights[i+di][j+dj]))):
                    min_effort[i+di][j+dj] = max_diff
                    heappush(heap, (max_diff, i+di, j+dj))

        return min_effort[-1][-1]
                    
            
            
            