from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        return len(set(i for i,j in Counter(words1).items() if j==1)&set(i for i,j in Counter(words2).items() if j==1))
        
        
                
        
        