class Solution:
    def compress(self, chars: List[str]) -> int:
        
        s = ""
        
        prev = ""
        count = 0
        for c in chars:
            if prev == c:
                count += 1
            else:
                s += prev + (str(count) if count>1 else "")
                count = 1
            prev = c
        s += prev + (str(count) if count>1 else "")
        
        
        chars[:] = s
        