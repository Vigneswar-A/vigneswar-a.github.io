class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        p1=min_=float('inf')
        p2=-p1
        for i in range(len(wordsDict)):
            if wordsDict[i]==word1:
                p1=i
            elif wordsDict[i]==word2:
                p2=i
            min_=min(min_,abs(p1-p2))
            
        return min_
            
                
                
        