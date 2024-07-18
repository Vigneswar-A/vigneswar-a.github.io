class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        arr.sort(key = lambda n : abs(n-x))
        return sorted(arr[:k])
        