class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        List=[]
        
        for word in words:
            if len(set(word))==len(set(pattern)):
                if word.translate(word.maketrans(word,pattern))==pattern:
                    List.append(word)
                
        return List
        