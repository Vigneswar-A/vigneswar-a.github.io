class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counts = Counter()
        left = 0
        distinct = 0
        res = 0
        
        for right in range(len(s)):
            counts[s[right]] += 1
            if counts[s[right]] == 1:
                distinct += 1
            while distinct > k:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    distinct -= 1
                left += 1
            res = max(res, right-left+1)
            
        return res
            
                
            