class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        window_sum = 0
        for i in range(k):
            window_sum += arr[i]
            
        res = ((window_sum // k) >= threshold)
        for j in range(k, len(arr)):
            window_sum -= arr[j-k]
            window_sum += arr[j]
            res += (window_sum // k) >= threshold
            
            
        return int(res)