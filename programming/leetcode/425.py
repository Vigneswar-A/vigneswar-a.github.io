class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words[0])
        
        root = (Trie := lambda : defaultdict(Trie))()
        
        for word in words:
            reduce(dict.__getitem__, word, root)['*']
            
        def get(prefix, node=root):
            curr = root
            for c in prefix:
                if c not in curr: return
                curr = curr[c]
                
            stack = [(prefix, curr)]
            while stack:
                prefix, node = stack.pop()
                if '*' in node:
                    yield prefix
                for i in node:
                    stack.append((prefix+i, node[i]))
                    
        sequence = []
        res = []
        def backtrack():
            if len(sequence) == n:
                yield sequence[:]
                return
            
            j = len(sequence)
            for word in get(''.join(sequence[i][j] for i in range(j))):
                sequence.append(word)
                yield from backtrack()
                sequence.pop()
                
        return [*backtrack()]

                
            
