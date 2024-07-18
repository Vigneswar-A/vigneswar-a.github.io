class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        Trie = lambda : defaultdict(Trie)
        
        root = Trie()
        
        for word in words:
            reduce(defaultdict.__getitem__, word, root)['*']
        
        res = ''
        def dfs(node = root, s = ''):
            nonlocal res
            
            if len(s)>len(res):
                res = s
            elif len(s) == len(res) and res > s:
                res = s
                
    
            for child in node:
                if '*' in node[child]:
                    dfs(node[child], s+child)
                    
        dfs()

        return res
                   
                
        
       

            
           
