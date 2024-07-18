class Solution:
    def beautySum(self, s: str) -> int:

        counts = [0] * 26
        res = 0

        for i in range(len(s)):
            minf = inf
            maxf = -inf
            for j in range(i, len(s)):
                counts[ord(s[j]) - ord('a')] += 1
                minf = min(set(counts).difference({0}))
                maxf = max(set(counts).difference({0}))
                res += abs(maxf-minf)
            counts = [0]*26
        return res
