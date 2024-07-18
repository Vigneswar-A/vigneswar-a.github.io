class Solution:
    
    @cache
    def rearrangeSticks(self, n: int, k: int) -> int:
        
        
        # if number of sticks = number of increment the arrangement should be ascending
        if n == k:
            return 1
        
        # if no more increments, its impossible to place anymore elements as n > k
        if k == 0:
            return 0
        
        ans = 0
        
        # case 1 - we place highest number than before
        ans += self.rearrangeSticks(n-1, k-1)
        
        # case 2 - we place any other number
        ans += (n-1) * self.rearrangeSticks(n-1, k)
        
        
        return ans%(1000_000_007)
        
        
            