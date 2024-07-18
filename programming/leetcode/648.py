class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = {}
        for word in dictionary:
            curr = root
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['*'] = '*'
          
        res = sentence.split()
        
        for i , word in enumerate(res):
            curr = root
            temp = ''
            for c in word:
                if '*' in curr:
                    res[i] = temp
                    break
                elif c in curr:
                    curr = curr[c]
                    temp += c          
                else:
                    break
                    
        return ' '.join(res)
            
                
            
        