class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        s = s.lower()
        count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(len(s)//2):
            count += (s[i] in vowels)
            count -= (s[-i-1] in vowels)
        return count == 0
        