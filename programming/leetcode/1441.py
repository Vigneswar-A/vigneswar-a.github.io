class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        count = 0
        while a or b or c:
            a_bit = a&1
            b_bit = b&1
            c_bit = c&1

            if a_bit and b_bit and not c_bit:
                count += 2
            elif a_bit and not b_bit and not c_bit:
                count += 1
            elif not a_bit and b_bit and not c_bit:
                count += 1
            elif not a_bit and not b_bit and c_bit:
                count += 1
            a //= 2
            b //= 2
            c //= 2
            
        return count
                