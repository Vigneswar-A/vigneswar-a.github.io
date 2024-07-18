class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        window=len(s)
        
        while window>0:
            for i in range(len(s)-window+1):
                current=s[i:window+i]
                if all(i.upper() in current and i.lower() in current for i in set(current.lower())):
                    return current
            window-=1
                        
                
        return ''
        