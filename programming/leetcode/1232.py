class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        key = lambda n : sum(min(n,i) for i in arr)
        
        left = 0
        right = max(arr)
        while left <= right:
            mid = left+right >> 1
            
            if key(mid) < target:
                left = mid+1
            elif key(mid):
                right = mid-1
            
           
     
        
   
        return left if abs(key(left-1)-target) > abs(key(left)-target) else left-1
       

        