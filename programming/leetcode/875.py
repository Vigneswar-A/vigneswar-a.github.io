class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        
        res = -1   
        left = right = 0
        size = len(arr)-1
        
        while left < size:
            flag = False
            while right < size and arr[right] < arr[right+1]:
                right += 1
                flag = True
            
            flag2 = False
            while right < size and arr[right] > arr[right+1]:
                right += 1
                flag2 = True
                    
            if flag and flag2:           
                res = max(right-left , res)
            
            while right < size and arr[right] == arr[right+1]:
                right += 1
                
            left = right

        return res+1