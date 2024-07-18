class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        size = len(s)
        left = 0
        counts = Counter()
        ans = 0
        
        for right in range(size):
            counts[s[right]] += 1
            while left < right and (right-left - max(counts.values())) >= k:
                counts[s[left]] -= 1
                left += 1
                
            ans = max(ans, right-left+1)
            
        return ans
                
            
        