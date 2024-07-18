parse = re.compile(r'^(-*\d+)\+([-+]{0,1}\d+)i$')
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1 , i1 = map(int , parse.fullmatch(num1).groups())
        r2 , i2 = map(int , parse.fullmatch(num2).groups())
        
        real = r1*r2 - i1*i2
        img = r1*i2 + i1*r2
        
        return f"{real}+{img}i"
        
        
        