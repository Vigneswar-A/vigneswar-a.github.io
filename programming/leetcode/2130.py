class Solution:
    def maxProduct(self, string: str) -> int:
        
        
        def bruteforce(i=0, s='', t=''):
            res = 0
            if s == s[::-1] and t == t[::-1]:
                res = len(s)*len(t)
            if i == len(string):
                return res
            return max(res, bruteforce(i+1, s+string[i], t), bruteforce(i+1, s, t+string[i]), bruteforce(i+1, s, t))
        
        return bruteforce()
            