class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        
        def get_divisors(n):
            for i in range(1, int(n**0.5) + 1):
                if n%i == 0:
                    yield (n//i - i, i, n//i)
                    
        return min(*get_divisors(num+1), *get_divisors(num+2))[1:]
        