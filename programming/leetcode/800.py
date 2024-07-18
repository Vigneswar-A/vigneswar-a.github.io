class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        n = len(s)
        
        def backtrack(s, start=0):
            if start > n:
                return None
            yield s
            for i in range(start, n):
                if s[i].isalpha():
                    yield from backtrack(s[:i] + s[i].swapcase() + s[i+1:], i+1)
                    
        return tuple(backtrack(s))
                
        