class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return map(names.__getitem__, sorted(range(len(heights)), key = heights.__getitem__, reverse = 1))
        