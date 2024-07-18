class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        
        def get_factors(num):
            yield -num
            for i in range(1 , int(num ** 0.5) + 1):
                if num % i == 0:
                    yield i
                    yield num // i
        
        return sum(get_factors(num)) == num
            
        