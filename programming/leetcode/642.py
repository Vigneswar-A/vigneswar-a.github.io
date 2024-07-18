class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = {}
        self.prefix = ''
        for sentence , time in zip(sentences , times):
            self.add(sentence , time)
               
    def add(self , word , time = 1):
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}     
            curr = curr[c]
            
        if '*' not in curr:
            curr['*'] = 0
        curr['*'] -= time
            
    def input(self, c: str) -> List[str]:
        curr = self.root
        
        if c == '#':
            self.add(self.prefix)
            self.prefix = ''
            return None
        
        self.prefix += c
               
        for i in self.prefix:
            if i in curr:
                curr = curr[i]
            else:
                return []
         
        words = []
        queue = [(self.prefix , curr)]
        
        while queue:
            word , node = queue.pop(0)
            for c in node:
                if c != '*':
                    queue.append((word + c , node[c]))
                else:
                    words.append((node['*'] , word))
              
        return [word for time , word in sorted(words)[:3]]
                
            
                
                
        
            
            
            
            
            
            
            
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)