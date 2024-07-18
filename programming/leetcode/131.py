class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(string = s, path = []):
            if string == '':
                res.append(path[:])
                return None
            
            if len(string) < 2:
                res.append(path+[string])
                return None
            
            for i in range(len(string)+1):
                
                if string[:i] == string[i-1::-1]:
                    path.append(string[:i])
                    backtrack(string[i:], path)
                    path.pop()
                    
            return None
        backtrack()
        return res
                
            