class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        
        odd = 0
        even = 0
        for i,c in enumerate(reversed(bin(n))):
            if i%2:
                odd += (c == '1')
            else:
                even += (c == '1')
        return [even, odd]
                
            
            
        