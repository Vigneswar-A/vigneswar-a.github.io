import re
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        return len(set(map(int,re.findall(r'[0-9]+',word))))
        