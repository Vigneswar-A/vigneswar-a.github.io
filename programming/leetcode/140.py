class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordDict = set(wordDict)
        n = len(s)
        res = []
        
        @cache
        def backtrack(i=0, path=()):
            if i == n:
                res.append(" ".join(path))
                return
            path = list(path)
            for j in range(i+1, n+1):
                if s[i:j] in wordDict:
                    path.append(s[i:j])
                    backtrack(j, tuple(path))
                    path.pop()
                    
        backtrack()
        return res
            
            