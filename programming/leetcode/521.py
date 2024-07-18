class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return a != b and max(len(a), len(b)) or -1
                
        