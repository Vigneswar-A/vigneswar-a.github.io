class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        mappings = {i : str(i) for i in range(10)}
        mappings.update({10 : "a", 11 : "b", 12 : "c", 13 : "d", 14 : "e", 15 : "f"})
        
        def to_binary(num):
            res = ""
            sign = 1
            if num < 0:
                sign = 0
                num = abs(num) - 1
                
            num = abs(num)
            
            while num:
                res += str(int(num%2 == sign))
                num //= 2
                
            return res[::-1].rjust(32 , str(int(not sign)))
        
        def to_hex(num):
            res = 0
            i = 0
            for c in num[::-1]:
                res += 2**i * int(c)
                i += 1
            return res
                
        
        binary = to_binary(num)
        s = ""
        for i in range(0, 32, 4):
            s += mappings[to_hex(binary[i:i+4])]
            
        while s[0] == "0":
            s = s[1:]
            
        return s
    
    
            
        
        
        
        
                