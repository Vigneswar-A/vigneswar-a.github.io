class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        
        i = 0
        j = 0
        ans = inf
        
        try:
            while True:
                while wordsDict[i] != word1:
                    i += 1
                while wordsDict[j] != word2 or j == i:
                    j += 1
                ans = min(ans, abs(j-i))
                if i < j:
                    i += 1
                else:
                    j += 1
                
        except:    
            return ans