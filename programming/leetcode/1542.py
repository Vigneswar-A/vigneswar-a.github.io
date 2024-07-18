class Solution:
    def maxPower(self, s: str) -> int:
        
        prev = None
        power = count = 0
        for c in s:
            if c == prev:
                count += 1
            else:
                power = max(count , power)
                count = 0
            prev = c
            
        return max(count ,power) + 1
                
        