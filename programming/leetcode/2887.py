class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_idx = []
        vowels = []
        
        for i,c in enumerate(s):
            if c.lower() in 'aeiou':
                vowels.append(c)
                vowel_idx.append(i)
                
        string_list = list(s)
        vowels.sort(reverse=1)
        
        for i in vowel_idx:
            string_list[i] = vowels.pop()
            
        return ''.join(string_list)
        
        