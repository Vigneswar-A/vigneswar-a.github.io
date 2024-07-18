class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        heapq.heapify(sticks)
        res = 0
        while len(sticks) > 1:
            first_stick = heapq.heappop(sticks)
            second_stick = heapq.heappop(sticks)
            res += first_stick + second_stick
            heapq.heappush(sticks, first_stick + second_stick)

        return res

