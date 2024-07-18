class Solution:
    def minimumKeypresses(self, s: str) -> int:
        res = 0
        factor = 1
        for i , n in enumerate(sorted(Counter(s).values() , reverse = 1)):
            if i >= 9 and i % 9 == 0:
                factor += 1
            res += n * factor
                
        return res
                
            
        