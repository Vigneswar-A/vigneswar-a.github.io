class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        a,b,c = sorted([a,b,c])
        
        
          
        
           
        
           
       
       

           
            
        
          
            
       

            


            

        left = 0
        right = 10**18
        
        n -= 1
        while left <= right:
            mid = left+right >> 1
            
            k = mid//a + mid//b + mid//c - mid//lcm(a,c) - mid//lcm(b,c) - mid//lcm(a,b) + mid//lcm(a,b,c)
            
            
        
           
            if k <= n:
                left = mid+1
            else:
                right = mid-1
                
                
                
        return left
                
        
        
        
        