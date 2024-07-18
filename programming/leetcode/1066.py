class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        
        def bin_search(left , right):
            while left <= right:

                mid = left + right >> 1

                if arr[mid] == mid:
                    return mid

                if arr[mid] > mid:
                    right = mid - 1

                else:
                    left = mid + 1
                
            return -1
        
        res = bin_search(0, len(arr)-1)
        prev = res
        
        while res != -1:
            prev = res
            res = bin_search(0, res-1)
            
        return prev
        
                
            