class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:

        res = 0
        for i in range(m, n+1):
            for perm in itertools.permutations(range(1, 10), i):
                s = ''.join(map(str, perm))
                if any(((j in s or j[::-1] in s) and (k not in s or s.index(k) > s.index(j[0]))) for j,k in zip(('17', '79', '93', '13', '28', '46', '19', '37'), '48625555')):
                    continue
                res += 1

        return res
