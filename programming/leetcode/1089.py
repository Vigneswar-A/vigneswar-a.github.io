class Solution:
    def removeVowels(self, s: str) -> str:            
        for i in ((s:=s.replace(i,'')) for i in 'aeiou'):
            pass
        return i
        