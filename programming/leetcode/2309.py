class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        
        
        def get_score(text):
            a_count = res = 0
            for c in text:
                if c == pattern[1]:
                    res += a_count
                if c == pattern[0]:
                    a_count += 1
                
            return res
                
        return max(map(get_score, (text+pattern[1], pattern[0]+text)))