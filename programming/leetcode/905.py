class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        n = len(arr)
        hashmap = {arr[i]:i for i in range(n)}
        
        memo = [[0]*n for _ in range(n)]
        
        def dp(i, j):
            if memo[i][j] != 0:
                return memo[i][j]
            if arr[i]+arr[j] in hashmap:
                memo[i][j] = max(1+dp(j, hashmap[arr[i]+arr[j]]), memo[i][j])
            return memo[i][j]
        
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                ans = max(ans, dp(i, j))
                
        return ans+2 if ans else 0
                