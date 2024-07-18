class Solution:
    def sortString(self, s: str) -> str:
        counts = Counter(s)
        res = ''
        while True:
            prev = res
            for d in [1, -1]:
                for c in string.ascii_lowercase[::d]:
                    if counts[c]:
                        res += c
                        counts[c] -= 1
            if res == prev:
                return res
                
                    
                
            
        