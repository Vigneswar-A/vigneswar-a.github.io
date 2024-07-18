class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keypair = {}
        for c in "qwertyuiop":
            keypair[c] = 1
        
        for c in "asdfghjkl":
            keypair[c] = 2
            
        for c in "zxcvbnm":
            keypair[c] = 3
            
        res = []
        for word in words:
            keyno = keypair[word[0].lower()]
            for c in word:
                if keypair[c.lower()] != keyno:
                    break
            else:
                res.append(word)
                
        return res
                
            
        
        
        