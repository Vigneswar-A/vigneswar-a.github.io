class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        for i in range(len(word)):
            if word[i] == ch:
                break
        else:
            return word
                
        return word[i::-1] + word[i+1:]
        