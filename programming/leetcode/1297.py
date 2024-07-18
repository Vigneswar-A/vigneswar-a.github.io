class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count={'b':0,'a':0,'l':0,'o':0,'n':0}
        
        for c in text:
            if c in ['b','a','n']:
                count[c]+=1
            elif c in ['l','o']:
                count[c]+=0.5
                
        return int(min(count.values()))
        
        