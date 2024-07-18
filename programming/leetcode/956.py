class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        
        @cache
        def dp(i, goal):
            if goal == 0:
                return i == 0
            return ((n-i+1)*dp(i-1, goal-1) + dp(i, goal-1)*max(i-k, 0))%(1000000007)
        
        return dp(n, goal)
        
        