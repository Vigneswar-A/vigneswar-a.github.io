from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return filter(lambda word:C[word]==1,C:=Counter(s1.split()+s2.split()))
        

                
        