class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        
        prev = arr[:]
        n = len(arr) - 1
        flag = True
        while flag:
            flag = False
            for i in range(1 , n):
                if arr[i - 1] > arr[i] < arr[i + 1]:
                    prev[i] += 1
                    flag = True
                elif arr[i - 1] < arr[i] > arr[i + 1]:
                    prev[i] -= 1
                    flag = True
            arr = prev[:]
            
            
        
        return arr
                
            
        