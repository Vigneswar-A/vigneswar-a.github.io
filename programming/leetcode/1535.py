class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        nums = []
        @cache
        def dp(n, m, k):
            if n == 1 and k == 1:
                return 1
            if n == 1:
                return 0
            res = 0
            
            #place a maximum element in current position
            for element in range(1, m):
                res += dp(n-1, element, k-1)
                
            #place a number smaller than maximum element in current position
            res += m*dp(n-1, m, k)
            
            return res%1000000007
        
        return sum(dp(n, i, k) for i in range(1, m+1))%1000000007
            
                
                
                    
                