class Solution:
    def countAsterisks(self, s: str) -> int:
        
        flag = True
        count = 0
        
        for c in s:
            if flag and c == '*':
                count += 1
            elif c == '|':
                flag = not flag
                
        return count
        