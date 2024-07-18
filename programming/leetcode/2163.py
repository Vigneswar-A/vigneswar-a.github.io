class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        valid=[]
        blocklist=[]
        for i in arr:
            if i not in valid and i not in blocklist:
                valid.append(i)
            else:
                try:
                    valid.remove(i)
                except:
                    pass
                blocklist.append(i)
        try:
            return valid[k-1]
        except:
            return ''
        
                
            
        