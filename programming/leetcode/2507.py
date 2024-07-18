class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        count = 0
        smaller, larger = sorted([a, b])
        
        for i in range(1, int(sqrt(smaller))+1):
            if smaller%i == 0 and larger%i == 0:
                count += 1
                
            if i != smaller//i and smaller%i == 0 and larger%(smaller//i) == 0:
                count += 1
                
                
        return count

        