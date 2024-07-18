class Solution:
    def closestFair(self, n: int) -> int:
        dig = int(log10(n))+1
        if dig%2 == 0:
            i = n if dig%2 == 0 else (10**dig)
            while sum(1 if c%2 else -1 for c in map(int, str(i))) != 0:
                i += 1
                if i > 10**dig:
                    return int('1' + '0'*((dig+2)//2) + '1'*((dig)//2))
            return i
        else:
            return int('1' + '0'*((dig+1)//2) + '1'*((dig)//2))
    
    