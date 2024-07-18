class Solution:
    def numSub(self, s: str) -> int:
        res = count = 0
        
        for i in s:
            if i == '1':
                count += 1
            else:
                res += count*(count+1)//2
                count = 0   
                
        return (res + count*(count+1)//2) % 1000000007
            
                
            
        