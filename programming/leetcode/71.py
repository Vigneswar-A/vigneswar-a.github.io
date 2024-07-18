class Solution:
    def simplifyPath(self, path: str) -> str:
        
        parsed = list(filter(None, re.split(r'(/+)|/(\.+)', path)))
        stack = []
        
        for c in parsed:
            if c == ".":
                pass
            elif c == "..":
                if stack:
                    stack.pop()
            elif set(c) == {"/"}:
                continue
            else:
                stack.append(c)

        return '/' + '/'.join(stack)
                
                