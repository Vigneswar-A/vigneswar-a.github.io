class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        words.sort(key=len, reverse=1)
        s = ''
        res = []
        
        for word in words:
            if word in s:
                res.append(word)
            s += '*' + word
            
            
        
        return res
            
            
        
     
        