class Solution:
    def passThePillow(self, n: int, time: int) -> int: 
        pos = time%(n-1)
        if (time//(n-1))%2 == 0:
            return pos+1
        return n-pos
        