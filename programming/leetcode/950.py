from collections import Counter
from math import gcd
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return all([len(deck)>1,gcd(*[j for i,j in Counter(deck).items()])>1])
        