class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        queue = deque([])
        visited = set()
        res = [[0]*n for _ in range(m)]
        
        h = 0
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    queue.append((i,j))
                    
        while queue:
            for _ in range(len(queue)):
                i,j = queue.popleft()
                if (i,j) in visited:
                    continue
                visited.add((i,j))
                res[i][j] = h
                for ni,nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= ni < m and 0 <= nj < n and (ni,nj) not in visited:
                        queue.append((ni, nj))
            h += 1
            
        return res
        