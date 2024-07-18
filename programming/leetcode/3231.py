class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        
        coins.sort()
        i = 0
        res = 0
        for x in coins:
            while i+1 < x:
                i = i*2+1
                res += 1
            i += x

        while i < target:
            i = i*2+1
            res += 1
        return res