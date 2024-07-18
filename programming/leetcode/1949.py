class DefDict(defaultdict):
    def __repr__(self):
        return dict.__repr__(self)
    
    
class Trie:

    def __init__(self):
        self.count = 0
        trie = lambda : DefDict(trie)
        self.root = trie()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr[c] 
            if '$' not in curr:
                curr['$'] = 0
            curr['$'] += 1
            
            
        if '*' not in curr:
            curr['*'] = 0
            
        curr['*'] += 1

        

    def countWordsEqualTo(self, word: str) -> int:
        curr = self.root
        for c in word:
            curr = curr[c]
        if '*' in curr:
            return curr['*']
        return  0

    def countWordsStartingWith(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            curr = curr[c]
        if '$' in curr:
            return curr['$']
        return 0


    def erase(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr[c]
            curr['$'] -= 1 
        curr['*'] -= 1
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)