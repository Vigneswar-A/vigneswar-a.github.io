class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        
        return max(map(lambda s : int(s) if s.isnumeric() else len(s), strs))
    
        