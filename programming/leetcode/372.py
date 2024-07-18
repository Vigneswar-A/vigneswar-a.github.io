class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        num = 0
        for n in b:
            num *= 10
            num += n
            
        return pow(a , num , 1337)
        