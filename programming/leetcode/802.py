class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        return sorted((arr[i]/arr[j], [arr[i], arr[j]])  for i in range(len(arr)) for j in range(i+1, len(arr)))[k-1][1]