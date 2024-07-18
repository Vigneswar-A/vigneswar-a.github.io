class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        counts = []
        for j in range(n):
            count = Counter()
            for i in range(m):
                count[grid[i][j]] += 1
            counts.append(count)
        print(counts)
            
        @cache
        def dp(i, prev):
            if i == n:
                return 0
            res = inf
            
            for j in list(counts[i])+[max(counts[i])+1000]:
                if j == prev:
                    continue
                res = min(res, dp(i+1, j)+(m-counts[i][j]))
            return res
        
        return dp(0, None)
                
                
        
        
        
        