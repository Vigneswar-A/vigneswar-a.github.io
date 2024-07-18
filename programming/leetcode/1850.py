class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s)-1

        while i < j and s[i] == s[j]:
            if i+1 < j and s[i+1] == s[i]:
                i += 1
            elif i < j-1 and s[j-1] == s[j]:
                j -= 1
            else:
                i += 1
                j -= 1
            if i == j:
                return 1
                
        return max(j-i+1, 0)
            
            