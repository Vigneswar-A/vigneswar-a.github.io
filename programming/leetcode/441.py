class Solution:
    series = [*accumulate(range(0, 100000))]
    def arrangeCoins(self, n: int) -> int:
        series = Solution.series
        left = 1
        right = n
        
        while left <= right:
            mid = left + right >> 1
            curr = mid*(mid+1) >> 1
            if curr == n:
                return mid
            elif curr > n:
                right = mid-1
            else:
                left = mid+1
        
        return right
                
        
        