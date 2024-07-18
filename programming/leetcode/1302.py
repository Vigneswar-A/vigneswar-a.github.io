class Solution:
    def makeFancyString(self, s: str) -> str:
        
        word = ''
        j = 0
        
        for i in s:
            if j >= 2 and word[-1] == i == word[-2]:
                continue
            word += i
            j += 1
            
        return word
            
            