
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        if set(s1)!=set(s2):return 0
        
        count=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                count+=1
        
        return count in [0,2]
        