from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return (c:=Counter(s).most_common())[0][1]==c[-1][1]