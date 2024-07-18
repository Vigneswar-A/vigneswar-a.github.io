class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        
        left = 0
        right = len(arr)
        
        while left <= right:
            mid = left+right >> 1
            
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            
            elif arr[mid-1] < arr[mid+1]:
                left = mid+1
            
            else:
                right = mid-1
                
                
        return mid
                
        