class Solution:
    def splitString(self, s: str) -> bool:
        
        @cache
        def dp(i=0, prev=-1):
            if i == len(s):
                return prev != int(s)
            
            for j in range(i+1, len(s)+1):
                if (prev == -1 or int(s[i:j]) == prev-1) and dp(j, int(s[i:j])):
                    return 1
            
            return 0
        
        return dp()
        