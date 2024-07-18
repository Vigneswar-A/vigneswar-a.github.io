class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:  
        if len(s) == k:
            return 0
        
        "baaaaa"
        2

        def get_length(cnt):
            if cnt == 0:
                return 0
            elif cnt == 1:
                return 1
            return len(str(cnt))+1
            
        n = len(s)

        @cache
        def dp(i=0, cnt=0, k=k):
            res = inf
            #delete j characters
            for j in range(k+1):
                if i+j+1 >= n:
                    return min(res, get_length(cnt+1))
                elif s[i] == s[i+j+1]:
                    res = min(res, dp(i+j+1, cnt+1, k-j))
                else:
                    res = min(res, dp(i+j+1, 0, k-j) + get_length(cnt+1))  
                    
            return res
                    
        res = inf
        for j in range(k+1):
            res = min(res, dp(j, 0, k-j))
        return res
                    
                    
                
                
            
            
            