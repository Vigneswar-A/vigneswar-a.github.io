class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        banned = sorted(set(banned))
        prefix = list(accumulate(banned))+[0]
        
        until = bisect.bisect(range(1, n+1), 0, key=lambda k : (k*(k+1)//2 - prefix[bisect.bisect(banned, k)-1]) > maxSum)
        return until - bisect.bisect(banned, until)