class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        balance = 0
        for c in s:
            if c == '(':
                balance += 1
            else:
                if balance:
                    balance -= 1
                else:
                    res += 1
               
                
        return res+balance
                
            
            
        