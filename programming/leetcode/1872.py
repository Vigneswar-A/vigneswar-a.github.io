class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        
        prefix = list(accumulate(candiesCount))
        return [(type == 0 or prefix[type-1]//cap <= day) and prefix[type] > day for type, day, cap in queries]

        