class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        
        res = set(range(2, n+1))
        x = 0
        i = 1
        while True:
            if ((x+k*(i))%n)%n+1 not in res:
                return res
            res.discard((x+k*(i))%n + 1)
            x = (x+k*(i))%n
            i += 1
        
        