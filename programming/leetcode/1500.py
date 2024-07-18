class Solution:
    def countLargestGroup(self, n: int) -> int:

        c = Counter()
        res = 0

        for i in range(1, n+1):
            key = sum(map(int, str(i)))
            c[key] += 1
            res = max(res, c[key])
        
        return sum(res==val for val in c.values())