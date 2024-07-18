from itertools import chain
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        return set(chain.from_iterable([range(arr[0],arr[1]+1) for arr in ranges]))>=set(range(left,right+1))
        