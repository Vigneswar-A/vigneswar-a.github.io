class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
        return accumulate(encoded , xor , initial = first)
            
        