precomp = [0]*(10**4+1)

for i in range(1, 10**4+1):   
    temp = i
    fives = 0
    while i:
        
        i //= 5
        fives += i
    precomp[temp] = fives


class Solution:
    def trailingZeroes(self, n: int) -> int:        
        return precomp[n]
                
        