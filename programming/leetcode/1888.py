class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        low = None
        low_idx = -1
        for idx, (px, py) in enumerate(points):
            if x == px or y == py:
                distance = abs(x - px) + abs(y - py)
                if low is None or low > distance:
                    low = distance
                    low_idx = idx
        return low_idx