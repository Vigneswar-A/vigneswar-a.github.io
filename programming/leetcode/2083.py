class Solution:
    def isThree(self, n: int) -> bool:
        
        divisors = set()
        for i in range(1, int(n**0.5)+1):
            if n%i == 0:
                divisors.add(n//i)
                divisors.add(i)
                
        return len(divisors) == 3
        