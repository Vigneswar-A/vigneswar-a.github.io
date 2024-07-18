import re
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        Indices=[]
        for word in words:
            matches=re.finditer(f"(?=({word}))",text)
            Indices.extend(((match.start(),match.start()+len(word)-1) for match in matches))
        
        return sorted(Indices)
        