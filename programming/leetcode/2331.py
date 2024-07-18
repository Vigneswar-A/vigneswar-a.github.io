class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        return sorted(reduce(set.intersection , map(set , nums)))
        
        