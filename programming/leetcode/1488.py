class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        @cache
        def power(n):
            if log(n , 2)%1==0:
                return log(n,2)
            if n%2 == 0:
                return 1+power(n//2)
            return 1+power(3*n+1)
        

        return sorted(range(lo , hi+1) , key = power)[k-1]