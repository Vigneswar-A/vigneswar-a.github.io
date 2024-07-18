class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        size = len(s)
        if size < 3:
            return size
        l , r = 0 , 0
        
        hashmap = {}
        max_len = 2
        while r < size:
            hashmap[s[r]] = r
            r += 1
            
            if len(hashmap) == 3:
                d = hashmap.pop(s[min(hashmap.values())])
                l = d + 1
            
            max_len = max(max_len , r - l)
            
        return max_len
        
                
            
            
        