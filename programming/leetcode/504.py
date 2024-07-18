class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return "0"
        
        s = ""
        sign = "" if num >= 0 else "-"
        num = abs(num)
        while num:
            s += str((num%7))
            num //= 7
            
        return sign+s[::-1]
            
        