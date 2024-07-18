class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        req_counts = Counter(t)
        req_distinct = len(set(t))
        
        counts = Counter()
        left = 0
        distinct = 0
        res = None
        for right in range(len(s)):
            counts[s[right]] += 1
            if s[right] in t and counts[s[right]] == req_counts[s[right]]:
                distinct += 1
               
            while distinct == req_distinct:
                if res is None or len(res) > right-left:
                    res = s[left:right+1]
                if s[left] in t and counts[s[left]] == req_counts[s[left]]:
                    distinct -= 1
                counts[s[left]] -= 1
                left += 1
                
        return res or ""

                    
            
                
            
            
