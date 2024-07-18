class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        n = len(s)
        letters = {}
        
        res = 0
        
        while right < n:
            
            if s[right] in letters:
                left = max(left , letters[s[right]] + 1)
                
            
            letters[s[right]] = right
            res = max(res , right - left + 1)
            right+= 1
            
        return res
            
            
            
        
                
                
            
        