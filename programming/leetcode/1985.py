class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        stack = []
        res = 0
        
        for n in nums:
            value = 0
            while stack and n < stack[-1][0]:
                prevnum, prevscore = stack.pop()
                value += prevscore
                res = max(res, prevnum*value)
            stack.append((n, value+n))

        value = 0
        while stack:
            prevnum, prevscore = stack.pop()
            value += prevscore
            res = max(res, prevnum*value)
            
        return res%mod
                
                