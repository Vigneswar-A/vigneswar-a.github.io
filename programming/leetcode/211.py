class mutabledict(dict):
    def __hash__(self):
        return id(self)
            
class WordDictionary:
    def __init__(self):
        self.root = {}
        

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['*'] = '*'
        self.search.cache_clear()
        return None
    
    @lru_cache
    def search(self, word: str , root = None) -> bool:
        
        if root is None:
            root = self.root
        curr = root
        for i in range(len(word)):
            if word[i] == '.':
                return any(self.search(word[i + 1:] , mutabledict(rt)) for rt in curr.values() if rt != '*')
            if word[i] not in curr:
                return False
            curr = curr[word[i]]
        return '*' in curr