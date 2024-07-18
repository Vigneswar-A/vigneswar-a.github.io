class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        stack = []
        counts = Counter(s)
        instack = set()

        for c in s:
            while stack and stack[-1] > c and counts[stack[-1]] > 1 and c not in instack:
                remove = stack.pop()
                counts[remove] -= 1
                instack.remove(remove)
                
            if c not in instack:
                stack.append(c)
                instack.add(c)
            else:
                counts[c] -= 1
            
        return ''.join(stack)
            