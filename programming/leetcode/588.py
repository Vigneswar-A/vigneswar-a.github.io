class FileSystem:

    def __init__(self):
        Trie = lambda : defaultdict(Trie)
        self.root = Trie()
        
    def ls(self, path: str) -> List[str]:
        currnode = self.root
        for word in filter(None, path.split('/')):
            currnode = currnode[word]
        if 'content' in currnode:
            return [word]
        return sorted(currnode.keys())

    def mkdir(self, path: str) -> None:
        currnode = self.root
        for word in filter(None, path.split('/')):
            currnode = currnode[word]
        
    def addContentToFile(self, filePath: str, content: str) -> None:
        currnode = self.root
        for word in filter(None, filePath.split('/')):
            currnode = currnode[word]
        if 'content' not in currnode: currnode['content'] = ''
        currnode['content'] += content

    def readContentFromFile(self, filePath: str) -> str:
        currnode = self.root
        for word in filter(None, filePath.split('/')):
            currnode = currnode[word]
        return currnode['content']
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)