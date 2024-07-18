class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        @cache
        def dp(i, m, n):
            if i == len(strs):
                return 0
            
            ans = 0
            if strs[i].count('0') <= m and strs[i].count('1') <= n:
                ans = 1 + dp(i+1, m-strs[i].count('0'), n-strs[i].count('1'))
                
            return max(ans, dp(i+1, m, n))
        
        return dp(0, m, n)
        