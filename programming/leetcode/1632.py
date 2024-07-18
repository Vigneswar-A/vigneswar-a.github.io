class Solution:
    def numSplits(self, s: str) -> int:
        
        prefix = []
        suffix = []
        seen = set()
        
        for c in s:
            seen.add(c)
            prefix.append(len(seen))
            
        seen.clear()
        for c in s[::-1]:
            seen.add(c)
            suffix.append(len(seen))
        suffix.reverse()
        
        ans = 0
        for i in range(len(s)-1):
            if prefix[i] == suffix[i+1]:
                ans += 1
                
        return ans
                
            
        
            
            