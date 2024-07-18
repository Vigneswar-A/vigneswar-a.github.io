class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:
        gain = (100 - loss)/100
        
        def is_possible(n):
            res = 0
            for i in buckets:
                diff = (i-n)
              
                if diff > 0:

                    res += diff*gain
                else:
                    res += diff
               

              
            
            return res >= 0
        



        left = 0
        right = max(buckets)
        acc = 0.000001
        while right-left>acc:
           
            mid = (left+right)/2
            if is_possible(mid):
                left = mid + acc
            else:
                right = mid - acc
                
                
                
        return left
        