class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        steps , temp , tot = 0 , [] , 0
        for i in (widths[ord(c) - 97] for c in s):
            if tot + i > 100:
                steps += 1
                tot , temp = 0 , []
            temp.append(i)
            tot += i
        return steps + 1 , sum(temp)
        
            
            
        