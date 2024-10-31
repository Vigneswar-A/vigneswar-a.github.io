class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = [(j,i) for i,j in enumerate(nums)]
        heapify(heap)
        visited = set()
        res = 0
        while heap:
            num, idx = heappop(heap)
            if idx in visited:
                continue
            res += num
            visited.add(idx+1)
            visited.add(idx-1)
        return res
            
        