class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        res = 0
        substrings = []
        def backtrack(s):
            nonlocal res
            res = max(res, len(set(substrings)))
            for i in range(1, len(s)+1):
                substrings.append(s[:i])
                backtrack(s[i:])
                substrings.pop()
                
        backtrack(s)
        return res
            
                