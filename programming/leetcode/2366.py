class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:

        heap = [cap-rock for cap,rock in zip(capacity,rocks)]

        heapq.heapify(heap)

        res = 0
        while additionalRocks > 0 and heap:
            to_remove = heapq.heappop(heap)
            if to_remove == 0:
                res += 1
            elif to_remove <= additionalRocks:
                additionalRocks -= to_remove
                res += 1
            else:
                break

        return res

