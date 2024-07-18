class Solution:
    def digitCount(self, num: str) -> bool:
        counts = Counter(num)
        return all(int(num[i]) == counts[str(i)] for i in range(len(num)))
        