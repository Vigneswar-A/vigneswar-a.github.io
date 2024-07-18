class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        count = sum_n = sum_arr = 0
        for i in range(len(arr)):
            sum_arr += arr[i]
            sum_n += i
            
            if sum_arr == sum_n:
                count += 1
                
        return count
            
        