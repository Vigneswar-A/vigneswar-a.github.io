class Solution:
    def maxDepth(self, s: str) -> int:
        i = res = 0
        
        for c in s:
            if c == '(':
                i += 1
            elif c == ')':
                res = res if res > i else i
                i -= 1
                
        return max(res , i)
                
        