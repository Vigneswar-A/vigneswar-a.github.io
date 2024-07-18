class Solution:
    def trimMean(self, arr: List[int]) -> float:
        
        n = int((5/100) * len(arr))
        arr.sort()
        return sum(arr[n:-n]) / (len(arr) - 2*n)