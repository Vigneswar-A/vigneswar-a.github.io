class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        return ''.join(sorted(s, key=lambda c : (counts.get(c), c), reverse=1))