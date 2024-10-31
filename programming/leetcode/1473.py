class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        vowels = 'aeiou'
        prefix = [0]*(len(s))
        indices = {0:-1}
        res = 0
        for i,c in enumerate(s):
            if c in vowels:
                prefix[i] = prefix[i-1]^(1 << vowels.index(c))
            else:
                prefix[i] = prefix[i-1]
            if prefix[i] in indices:
                res = max(res, i-indices[prefix[i]])
            else:
                indices[prefix[i]] = i
                
        
        return res
            