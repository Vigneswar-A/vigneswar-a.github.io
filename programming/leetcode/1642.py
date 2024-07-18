class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        res = 0
        empty = 0
        while numBottles:
            res += numBottles
            empty += (numBottles%numExchange)
            numBottles //= numExchange
            numBottles += (empty//numExchange)
            empty = empty%numExchange
            
        
        return res
        