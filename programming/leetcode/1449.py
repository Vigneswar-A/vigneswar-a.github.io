class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        return map(lambda s : ''.join(s).rstrip(), zip_longest(*s.split(), fillvalue = " "))
        