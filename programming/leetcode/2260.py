class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        res = [s[x : x+k] for x in range(0, len(s), k)]
        
        last_str = res[-1]
        
        if len(last_str) != k:
            last_str += fill * (k- len(last_str))
            
        res[-1] = last_str
                
        return res