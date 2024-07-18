class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        size = len(p)
        p_counts = Counter(p)
        s_counts = Counter(s[:size])
        res = []
        
        if p_counts == s_counts:
            res.append(0)
        
        for i in range(size, len(s)):
            s_counts[s[i-size]] -= 1
            s_counts[s[i]] += 1
            
            if p_counts == s_counts:
                res.append(i-size+1)
            
        return res
            