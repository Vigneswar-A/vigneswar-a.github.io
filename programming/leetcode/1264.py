class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)   
        return sum(not word&broken for word in map(set, text.split()))
                
        