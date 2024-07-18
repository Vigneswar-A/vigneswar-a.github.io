class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        prefix = list(accumulate(code))
        n = len(code)
        
        def get_sum(curr, k):
            if k < 0:
                if curr+k < 0:
                    return (prefix[curr-1] if curr else 0) + prefix[-1] - prefix[(curr+k)-1]
                return prefix[curr-1] - (prefix[curr+k-1] if curr+k else 0)
            if curr + k >= n:
                return prefix[-1] - prefix[curr] + prefix[(curr+k)%n]
            return prefix[curr+k] - prefix[curr]
            

        
        return [get_sum(i, k) for i in range(n)]