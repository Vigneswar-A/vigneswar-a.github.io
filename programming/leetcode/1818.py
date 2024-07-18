class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        def solve1(s):
            stack = []
            res = 0
            i = 0
            while i < len(s):
                if not stack or stack[-1] != 'a' or s[i] != 'b':
                    stack.append(s[i])
                    i += 1
                    continue
                while i < len(s) and s[i] == 'b' and stack and stack[-1] == 'a':
                    res += x
                    stack.pop()
                    i += 1
                    
            return res,''.join(stack)
        
        def solve2(s):
            stack = []
            res = 0
            i = 0
            while i < len(s):
                if not stack or stack[-1] != 'b' or s[i] != 'a':
                    stack.append(s[i])
                    i += 1
                    continue
                while i < len(s) and s[i] == 'a' and stack and stack[-1] == 'b':
                    res += y
                    stack.pop()
                    i += 1
            return res,''.join(stack)
        
        if x > y:
            res, s = solve1(s)
            res += solve2(s)[0]
        else:
            res, s = solve2(s)
            res += solve1(s)[0]
            
        return res