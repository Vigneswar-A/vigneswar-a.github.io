class Solution:
    def minDeletions(self, s: str) -> int:
        counts = Counter(Counter(s).values())
        res = 0
        flag = True
        while flag:
            flag = False
            for c in sorted(counts, reverse=1):
                if not c:
                    continue
                while counts[c] > 1:
                    counts[c] -= 1
                    counts[c-1] += 1
                    res += 1
                    flag = True

        return res