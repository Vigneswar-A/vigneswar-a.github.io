class Solution:
    def countVowels(self, word: str) -> int:
        
        vowels = set('aeiou')
        ans = 0
        n = len(word)
        for i in range(len(word)):
            if word[i] in vowels:
                ans += n + i*(n-i-1)
        return ans
            