class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        
        res = ''
        end = a+b
        while len(res) < end:
            if a < b:
                res += 'bba'
                b -= 2
                a -= 1
            if b < a:
                res += 'aab'
                a -= 2
                b -= 1
            if a == b:
                res += 'ab'
                a -= 1
                b -= 1
        return res[:end]

        