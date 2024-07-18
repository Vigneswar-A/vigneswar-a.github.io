class MapSum:

    def __init__(self):
        self.root = {}
        

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for c in key:       
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['val'] = val

    def sum(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            if c not in curr:
                return 0
            curr = curr[c]
            
        stack = [curr]
        res = 0
        while stack:
            node = stack.pop()
            if 'val' in node:
                res += node['val']
            stack.extend(i for i in node.values() if not isinstance(i , int))
            
        return res
            
            
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)