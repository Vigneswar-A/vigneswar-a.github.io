class Solution:
    def addMinimum(self, word: str) -> int:
        
        res = 0
        i = 0

        if word[-1] != 'c':
            word += 'c'
            res += 1
        for c in word:
            while 'abc'[i] != c:
                res += 1
                i = (i+1)%3
            i = (i+1)%3
            
        return res
            