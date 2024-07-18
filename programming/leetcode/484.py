class Solution:
    def findPermutation(self, s: str) -> List[int]:
    
        s = 'I' + s
        currmax = 0
        res = []
        i = 0
        while i < len(s):
            count = 1
            if s[i] == 'I':
                while i+1 < len(s) and s[i+1] != 'I':
                    i += 1
                    count += 1
                currmax += count
                res.extend(range(currmax,currmax-count,-1))
            i += 1
        return res