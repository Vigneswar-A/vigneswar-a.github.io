from itertools import groupby
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        group=[len(list(l)) for n,l in groupby(s)]
        return sum(min(t) for t in zip(group,group[1:]))
        