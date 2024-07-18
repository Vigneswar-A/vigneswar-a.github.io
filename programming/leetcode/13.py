class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        
        res = roman[s[-1]]
        for i in range(len(s) - 1):
            res += (roman[s[i]] if roman[s[i]] >= roman[s[i + 1]] else -roman[s[i]])
                     
        return res
            
        