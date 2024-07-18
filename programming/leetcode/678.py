class Solution:
    def checkValidString(self, s: str) -> bool:
        end = len(s)
        
        @cache
        def dp(i=0 , opens=0):
            if i == end:
                return opens == 0
            if s[i] == '(':
                return dp(i+1 , opens+1)
            if s[i] == ')' and opens > 0:
                return dp(i+1 , opens-1)
            if s[i] == '*':
                return opens > 0 and dp(i+1 , opens-1) or dp(i+1 , opens+1) or dp(i+1 , opens)
            return False
        
        return dp()
            
            
                
        