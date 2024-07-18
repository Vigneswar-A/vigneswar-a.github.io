class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even1 = []
        odd1 = []
        even2 = []
        odd2 = []
        
        for i,(a,b) in enumerate(zip(s1, s2)):
            if i%2:
                odd1.append(s1[i])
                odd2.append(s2[i])
            else:
                even1.append(s1[i])
                even2.append(s2[i])
                
        odd1.sort()
        odd2.sort()
        even1.sort()
        even2.sort()
        
        return odd1 == odd2 and even1 == even2
            
        