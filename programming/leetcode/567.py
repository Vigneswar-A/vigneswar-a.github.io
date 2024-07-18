class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        size = len(s1)
        counts = Counter(s1)
        
        window = Counter(s2[:size])
        
        if window == counts:
            return True
        
        for i in range(size, len(s2)):
            window[s2[i-size]] -= 1
            window[s2[i]] += 1
            
            if window == counts:
                return True
            
        return False
        