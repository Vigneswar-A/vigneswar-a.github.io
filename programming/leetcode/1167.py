class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        blocks.sort(reverse=1)
        n = len(blocks)+1
        memo = [[-1]*n for w in range(n)]
        
        
        def dp(i=0, w=1):
            if w >= n-i-1:
                return blocks[i]
            if memo[i][w] != -1:
                return memo[i][w]
            if i == n-1:
                return 0
            if w == 0:
                return inf
            
            memo[i][w] = min(max(dp(i+1, w-1), blocks[i]), dp(i, 2*w)+split)
            return memo[i][w]
        
        return dp()