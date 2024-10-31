class Solution:
    def splitNum(self, num: int) -> int:
        digits = sorted(map(int, str(num)))
        res = 0
        carry = 0
        p = 1
        while digits:
            if len(digits) > 1:
                carry, add = divmod(digits.pop()+ digits.pop()+carry, 10)
                res += add*p
                p *= 10
            else:
                return res+(digits.pop()+carry)*p
            
                
        return res+carry*10
                
                
        
        
        
        