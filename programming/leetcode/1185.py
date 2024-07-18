# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mount: 'MountainArray') -> int:
        
        # find the pivot
        left = 1
        right = mount.length()-2
        
        while left <= right:
            mid = left+right >> 1
            if mount.get(mid-1) < mount.get(mid):
                left = mid+1
            else:
                right = mid-1
                
        pivot = left-1

        left = 0
        right = pivot
        while left <= right:
            mid = left+right >> 1
            x = mount.get(mid)
            if x < target:
                left = mid+1
            elif x > target:
                right = mid-1
            else:
                return mid
            
        left = pivot
        right = mount.length()-1
        while left <= right:
            mid = left+right >> 1
            x = mount.get(mid)
            if x > target:
                left = mid+1
            elif x < target:
                right = mid-1
            else:
                return mid
            
        return -1
            
        