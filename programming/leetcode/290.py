class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        
        if len(words)!=len(pattern):
            return False
        
        wordToletter = {}
        letterToword = {}
        
        for letter,word in zip(pattern , words):
            
            if letter in letterToword and letterToword[letter] != word:
                return False
            
            if word in wordToletter and wordToletter[word] != letter:
                return False
            
            letterToword[letter] = word
            wordToletter[word] = letter
                          
            
        return True