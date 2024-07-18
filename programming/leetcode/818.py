class Solution:
    def similarRGB(self, color: str) -> str:
        
        res = '#'
        for i in range(1, 6, 2):
            res += hex(round(int(color[i:i+2], 16)/17))[-1]*2
            
        return res
            
            
            
        