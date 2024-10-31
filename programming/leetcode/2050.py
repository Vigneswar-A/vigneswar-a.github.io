class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        even = n//2+n%2
        odd = n//2
        mod = 1000000007
        return (pow(5, even, mod)*pow(4, odd, mod))%mod
        