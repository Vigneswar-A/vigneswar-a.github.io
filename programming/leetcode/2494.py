class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        Trie = lambda : defaultdict(Trie)
        root = Trie()
        for word in words:
            node = root
            prefix = ''
            for c in word:
                node = node[c]
                if '*' not in node:
                    node['*'] = 0
                node['*'] += 1
                
                
        res = [0] * len(words)
        for i, word in enumerate(words):
            node = root
            for c in word:
                node = node[c]
                res[i] += node['*']
                
                
        return res
                            
                
            
            
        