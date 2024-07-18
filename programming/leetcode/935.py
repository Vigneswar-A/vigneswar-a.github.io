class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(s))
        else:
            s = deque(s)
            res = list(s)
            for i in range(len(s)):
                s.append(s.popleft())
                res = min(res, list(s))
            return ''.join(res)
            
                