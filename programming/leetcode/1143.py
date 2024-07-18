class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        return min(reduce(set.intersection, map(set, mat)), default=-1)