class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        
        table = [True] * (n+1)
        count = 0
        
        for i in range(2, n+1):
            if table[i] is True:
                for i in range(i*i, n+1, i):
                    table[i] = False
                count += 1
                

        return (factorial(count)*factorial(n-count))%1000000007
                
        