class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return ''.join(next(zip(*sorted(zip(s, indices), key = lambda a:a[1]))))