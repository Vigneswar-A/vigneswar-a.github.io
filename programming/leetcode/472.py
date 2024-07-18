class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        
        Trie = lambda : defaultdict(Trie)
        
        root = Trie()
        
        for word in words:
            reduce(dict.__getitem__, word, root)['*']
            
        def dfs(word, breaks=0):
            if not word:
                return breaks
            
            curr = root
            res = 0
            for i in range(len(word)):
                if word[i] in curr:
                    curr = curr[word[i]]
                else:
                    return res
                
                if '*' in curr:
                    res = max(res, dfs(word[i+1:], breaks+1))
                    
            return res
 
        return list(filter(lambda word : dfs(word) > 1, words))
                
            
            
            
            
            
        
            
        
        
        
                
                
                
        