class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        counts = Counter(chain.from_iterable(map(accumulate, wall)))
        max_ = max(counts)
        total = counts[max_]
        del counts[max_]
        return total-max(counts.values(), default=0)