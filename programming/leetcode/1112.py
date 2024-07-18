from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars=Counter(chars)
        output=0
        for i in words:
            if (current:=Counter(i)) & chars==current:output+=len(i)                
        return output
        