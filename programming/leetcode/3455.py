class Solution:
    def minimumLength(self, s: str) -> int:
        indices = defaultdict(deque)

        for i,c in enumerate(s):
            indices[c].append(i)

        res = 0
        for c in string.ascii_lowercase:
            while len(indices[c]) >= 3:
                indices[c].popleft()
                indices[c].pop()
            res += len(indices[c])
        return res


        