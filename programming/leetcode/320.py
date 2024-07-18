class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        res = []
        n = len(word)
        
        def backtrack(i=0, s = '', skipped=0):
            if i < n:
                backtrack(i+1, s, skipped+1)
                backtrack(i+1, s+(str(skipped) if skipped else '')+word[i])
            else:
                res.append(s + (str(skipped) if skipped else ''))

        backtrack()        
        return res
                
            
                