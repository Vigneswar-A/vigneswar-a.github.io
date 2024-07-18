powers = {tuple(sorted(str(2**i))) for i in range(32)}
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return tuple(sorted(str(n))) in powers
        
        