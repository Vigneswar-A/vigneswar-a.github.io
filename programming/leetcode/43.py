class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def get_num(s):
            num = 0
            power = len(s)-1
            
            for c in s:
                num += (ord(c) - ord('0'))*10**power
                power -= 1
                
            return num
        

        prod = get_num(num1) * get_num(num2)
        res = ''
        
        while prod:
            res = chr((prod%10)+ord('0'))+res
            prod //= 10
            
        return res or '0'
        