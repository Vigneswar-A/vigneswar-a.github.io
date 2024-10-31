class Solution:
    def countKeyChanges(self, s: str) -> int:
        
        return sum(1 for i in groupby(s.lower()))-1
        