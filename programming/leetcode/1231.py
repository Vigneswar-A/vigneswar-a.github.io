from collections import deque
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        o=deque()
        for i in range(len(arr)):
            o.append(max(arr[i+1::],default=-1))
        return o