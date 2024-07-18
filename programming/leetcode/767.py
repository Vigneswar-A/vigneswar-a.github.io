class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        primes = set()
        for i in range(2, 32):
            for j in range(2, isqrt(i)+1):
                if i%j == 0:
                    break
            else:
                primes.add(i)
        return sum(i.bit_count() in primes for i in range(left, right+1))
        