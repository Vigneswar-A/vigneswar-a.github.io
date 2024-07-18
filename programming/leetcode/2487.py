class Solution:
    def partitionString(self, s: str) -> int:
        
        seen = set()
        def backtrack(idx=0):
            if idx == len(s):
                return 1
            
            if s[idx] in seen:
                seen.clear()
                return 1 + backtrack(idx)
            
            seen.add(s[idx])
            
            return backtrack(idx+1)
            
        return backtrack()
            