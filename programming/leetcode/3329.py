class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        Trie = lambda : defaultdict(Trie)
        root = Trie()
        for num in arr1:
            reduce(dict.__getitem__, str(num), root)
        
        res = 0
        for num in arr2:
            node = root
            length = 0
            for c in str(num):
                if c not in node:
                    break
                node = node[c]
                length += 1
            res = max(length, res)
                
        return res
                
                