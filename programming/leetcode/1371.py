class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        opens = 0
        res = ''
        for c in s:
            if c == '(':
                opens += 1
            elif c == ')':
                if opens:
                    opens -= 1
                else:
                    continue
            res += c
        
        # remove unclosed opens
        ans = ''
        for c in res[::-1]:
            if c == '(' and opens:
                opens -= 1
                continue
            ans = c+ans
        return ans
                    