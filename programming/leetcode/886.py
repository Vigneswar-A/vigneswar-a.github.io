class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        def dp(l, r):
            if l >= r:
                return 0
            x = 0
            for i in range(l, r+1):
                if s[i] == '(':
                    x += 1
                else:
                    x -= 1
                if x == 0:
                    break
                    
            if l+1 == i:
                return 1+dp(i+1, r)
            return 2*dp(l+1, i-1)+dp(i+1, r)
        
        return dp(0, len(s)-1)
            
        