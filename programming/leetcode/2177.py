from collections import Counter
from itertools import chain
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        A=Counter(word1)
        B=Counter(word2)
        return not any((n>3 for n in chain((A-B).values(),(B-A).values())))
        
        