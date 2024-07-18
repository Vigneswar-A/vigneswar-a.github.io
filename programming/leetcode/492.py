class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        res = [inf, -inf]
        for i in range(1, int(area**0.5)+1):
            if area%i == 0:
                right,  left = sorted([i, area//i])
                if res[0]-res[1] > left-right:
                    res = [left, right]

        return res


