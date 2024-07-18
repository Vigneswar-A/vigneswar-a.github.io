class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        iterator = iter(string.ascii_lowercase)
        seen = set()
        mapping = {}
        
        for c in key:
            if c not in seen and c != ' ':
                mapping[c] = next(iterator)
            seen.add(c)
                
        return ''.join(map(lambda c : mapping[c] if c != ' ' else ' ', message))
                
                
        