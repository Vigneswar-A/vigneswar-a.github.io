class Solution:
    def expand(self, s: str) -> List[str]:
        
        words = ['']
        flag = False
        for c in s:
            if c == ',':
                continue
                
            elif c in '{}':
                flag = not flag
                temp = [*words]
                continue
                
            if flag:
                for word in temp:
                    words.append(word + c)
            else:
                words[:] = map(lambda word: word + c , words)
        
        maxsize = len(max(words , key = len))
        return sorted(word for word in words if len(word) == maxsize)
            
            
                
            