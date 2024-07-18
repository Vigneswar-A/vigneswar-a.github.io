class Solution:
    def largestPalindromic(self, num: str) -> str:
        
        digits = Counter(map(int, num))
        mid = max((i for i,c in digits.items() if c%2), default=None)

        res = ''
        if mid is not None:
            digits[mid] -= 1
            res = str(mid)
            

        for i,c in sorted(digits.items()):
            s = str(i)*(c//2)
            res = s+res+s
            
        while len(res) and res[0] == '0':
            res = res[1:-1]
            
        return res or '0'
            
        