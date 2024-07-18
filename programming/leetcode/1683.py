class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort(reverse=1)
        n = 2*len(piles)//3
        i = 1
        res = 0
        while i <= n:
            res += piles[i]
            i += 2
        
        return res
            
            