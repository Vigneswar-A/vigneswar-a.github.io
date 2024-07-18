from math import comb
from collections import Counter
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        return sum(comb(count,2) for ele,count in Counter(map(frozenset,dominoes)).items())
            
     