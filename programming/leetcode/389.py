from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return tuple((Counter(t)-Counter(s)).items())[0][0]
        
        
        