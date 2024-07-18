class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        for i in range(len(shifts)-2, -1, -1):
            shifts[i] += shifts[i+1]
            
        res = ''
        for i,c in enumerate(s):
            res += chr(97+(ord(c)-97+shifts[i])%26)
            
        return res
            
            
        
        