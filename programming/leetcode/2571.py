class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        prefix = list(accumulate(range(1, n+1)))

        for i in range(1, n):
            if prefix[i] == prefix[-1] - prefix[i-1]:
                return i+1
            
        return -1
            
        
        