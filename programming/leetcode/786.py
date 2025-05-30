# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
    
        left,right = 0,10**4
        
        while left <= right:
            
            mid = left + right >> 1
            num = reader.get(mid)
            
            if num == target:
                return mid
                
            elif num > target:
                right = mid - 1
                
            else:
                left = mid + 1
                
                
        return -1
                
        
        