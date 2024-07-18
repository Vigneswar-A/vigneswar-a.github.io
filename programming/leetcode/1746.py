class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        visited = {}
        res = -1
        
        for i,c in enumerate(s):
            if c in visited:
                res = max(res, i-visited[c]-1)
            else:
                visited[c] = i
        
        return res
        