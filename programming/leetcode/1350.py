class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        folders.sort(key=len)
        res = []
        Trie = lambda : defaultdict(Trie)
        root = Trie()
        
        for folder in folders:
            temp = root
            for c in folder:
                if '*' in temp and c == '/':
                    break
                temp = temp[c]
            else:
                res.append(folder)
            temp['*'] = '*'
        return res
        