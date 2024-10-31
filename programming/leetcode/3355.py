class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        points = list(accumulate(map(lambda i:i or -1, possible)))
        
        try:
            for i,j in enumerate(points):
                if j>(points[-1]//2):
                    res = i+1
                    break
            return res if res <= len(points)-1 else -1
        except:
            return -1
        
        
        
        

        
        