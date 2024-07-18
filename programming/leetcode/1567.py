class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a' , 'e' , 'i' , 'o' , 'u'}
        prefix = {}
        count = 0
        
        prefix[0] = 0
        for i in range(size := len(s)):
            if s[i] in vowels:
                count += 1
            prefix[i + 1] = count
            
        maxcount = 0
        for i in range(size - k + 1):
            maxcount = max(prefix[i + k] - prefix[i], maxcount)
            
        
        return maxcount
            
            
        