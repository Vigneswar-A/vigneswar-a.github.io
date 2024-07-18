class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if (size:=len(s))<k:
            return 0
        
        count=0
        for i in range(size-k+1):
            if len(set(s[i:i+k]))==k:
                count+=1
                
        return count