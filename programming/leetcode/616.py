class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        indices = []
        for word in words:
            for i in range(n-len(word)+1):
                if word == s[i:i+len(word)]:
                    indices.append((i, i+len(word)-1))
                    
        indices = self.merge(indices)
        s = list(s)
        for i,j in indices:
            s[i] = '<b>' + s[i]
            s[j] = s[j] + '</b>'
        return ''.join(s)
            
            
        
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        lo,hi = intervals[0]
        res = []
        for i,j in intervals:
            if i <= hi+1:
                hi = max(hi, j)
            else:
                res.append((lo, hi))
                lo, hi = i, j
        res.append((lo, hi))
        return res
        
        

            
            