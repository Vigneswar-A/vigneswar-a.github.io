class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        
        @cache
        def dp(i=0):
            if i == n:
                return 1
            
            ans = 0
            
            # single digit
            if s[i] == '*':
                ans += 9 * dp(i+1)
            elif s[i] != '0':
                ans += dp(i+1)
                
            if i+1 == n:
                return ans
            
            # double digit
            
            # normal 2 digit number
            if s[i] != '*' and s[i+1] != '*' and s[i] != '0' and int(s[i:i+2]) <= 26:
                ans += dp(i+2)
                
            # first digit is a *
            if s[i] == '*' and s[i+1] != '*':
                if int(s[i+1]) <= 6:
                    ans += 2*dp(i+2) # *5 -> 15 or 25
                else:
                    ans += dp(i+2)  # *7 -> 17
                    
            # second digit is a *
            if s[i] != '*' and s[i+1] == '*':
                if s[i] == '1':
                    ans += 9*dp(i+2) # 11, 12 .. 19
                if s[i] == '2':
                    ans += 6*dp(i+2) # 21, 22 .. 26
                    
            # both digit are *
            if s[i] == '*' and s[i+1] == '*':
                ans += 15*dp(i+2)
                

            return ans%1000000007
            
        return dp()
                
        