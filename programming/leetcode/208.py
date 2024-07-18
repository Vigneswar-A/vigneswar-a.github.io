class Trie:

    def __init__(self):
        self.trie = lambda : defaultdict(self.trie)
        self.root = self.trie()

        
        

    def insert(self, word: str) -> None:
        reduce(defaultdict.__getitem__, word, self.root)['*'] = '*'
        

    def search(self, word: str) -> bool:
        currnode = self.root
        for c in word:
            if c not in currnode:
                return False
            currnode = currnode[c]

        return '*' in currnode
        

    def startsWith(self, prefix: str) -> bool:
        currnode = self.root
        for c in prefix:
            if c not in currnode:
                return False
            currnode = currnode[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)