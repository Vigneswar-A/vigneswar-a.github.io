class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        
        def possible(maxlength):
            pieces = 0
            for i in ribbons:
                pieces += i//(maxlength)
                if pieces >= k:
                    return 0
            return 1
        return bisect.bisect(range(1, 100001), 0, key=possible)
        
        
                
        