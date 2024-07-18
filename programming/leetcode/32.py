class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        res = 0
        opens = 0
        start = 0
        for i,c in enumerate(s, 1):
            if c == '(':
                opens += 1
            elif opens:
                opens -= 1
            else:
                start = i

            if opens == 0:
                res = max(res, i-start)
                
        opens = 0
        start = 0
        for i,c in enumerate(reversed(s), 1):
            if c == ')':
                opens += 1
            elif opens:
                opens -= 1
            else:
                start = i

            if opens == 0:
                res = max(res, i-start)

        return res
            
        
        
                    
            
            