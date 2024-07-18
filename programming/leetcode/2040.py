class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        fee = [float("inf") for i in range(n)]# the final fee
        heap, graph = [(0, passingFees[0], 0)], collections.defaultdict(list)
        for start, end, time in edges:
            graph[start].append((end, time))
            graph[end].append((start, time))
        while heap:
            curTime, curFee, curNode = heappop(heap)
            if fee[curNode] <= curFee:
                continue
            fee[curNode] = curFee
            for neighbor, time in graph[curNode]:
                if time + curTime <= maxTime:
                    heappush(heap, (time + curTime, curFee + passingFees[neighbor], neighbor))
        return fee[-1] if fee[-1] != float("inf") else -1