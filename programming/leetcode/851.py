class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        res = []
        vowels = {'a', 'e', 'i', 'o', 'u'}
        words = sentence.split()
        
        for i in range(len(words)):
                
            if words[i][0].lower() in vowels:
                res.append(words[i] + 'ma' + 'a' * (i + 1))
            
            else:
                res.append(words[i][1:] + words[i][0] + 'ma' + 'a' * (i + 1))
                
                
        return ' '.join(res)
                
        