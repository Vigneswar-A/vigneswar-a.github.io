class Solution:
    def oddString(self, words: List[str]) -> str:
        
        values = {c:i for i,c in enumerate(ascii_lowercase)}
        
        prev = None
        flag = False
        for i in range(len(words)):
            curr = [values[words[i][j+1]] - values[words[i][j]] for j in range(len(words[i])-1)]
            if prev is None:
                prev = curr
            elif prev != curr:
                if flag is False:
                    flag = True
                else:
                    return words[i-1]
            elif flag:
                return words[i-2]
            prev = curr
                
        return words[-1]
            
        
                
                
        