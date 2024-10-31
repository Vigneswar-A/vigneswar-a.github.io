class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        
        l = 0
        rt = 1
        prev = None
       
        while rt <= len(message):
            rt *= 10
            prev = None  
                      
            r = rt
            l = 0
            while l <= r:
                k = l+r >> 1
                res = []
                i = 0
                j = 1
            
                if k == prev:
                    break
                prev = k
                while i < len(message):
                    suffix = f'<{j}/{k}>'
                    res.append(message[i:i+limit-len(suffix)]+suffix)
                    
                    if len(suffix) >= limit:
                        break
                    i += limit-len(suffix)
                    j += 1
            
            
                
                if i < len(message):
                    r = k-1
                    continue
                
                if len(res) < k:
                    r = k-1
                elif len(res) > k:
                    l = k+1
                else:
                    return res
            
            
            
        
        
            
        