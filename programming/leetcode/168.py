class Solution:
    def convertToTitle(self, col: int) -> str:
        hashmap = dict(enumerate(ascii_uppercase, 1))
        
        res = ''
        while col:
            
            if col%26 == 0:
                res += 'Z'
                col -= 1
            else:
                res += hashmap[(col%26)]
            
            col //= 26
            
        return res[::-1]
            
            
        