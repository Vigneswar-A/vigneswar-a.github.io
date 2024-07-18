class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        def is_strong(s):
            if len(s) < 8:
                return False          
            lower = upper = digit = special = False
            
            if s[0].isdigit():
                digit = True
            elif not s[0].isalnum():
                special = True
            elif s[0].isupper():
                upper = True
            else:
                lower = True
                
            for i in range(1, len(s)):
                if s[i-1] == s[i]:
                    return False
                if s[i].isdigit():
                    digit = True
                elif not s[i].isalnum():
                    special = True
                elif s[i].isupper():
                    upper = True
                else:
                    lower = True
                    
            return lower and upper and digit and special
        
        return is_strong(password)