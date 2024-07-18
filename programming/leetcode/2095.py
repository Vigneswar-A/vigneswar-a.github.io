class Solution:
    def minSwaps(self, s: str) -> int:      
        opens = 0
        swaps = 0
        for c in s:
            if c == "[":
                opens += 1
            elif c == "]":
                if opens <= 0:
                    swaps += 1
                    opens += 1
                else:
                    opens -= 1
        return swaps
                    
                    
                    
            
        