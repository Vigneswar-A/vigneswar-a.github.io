class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        
        apples = 0
        curr = 0
        i = 0
       
        while apples<neededApples:
            
            curr = curr+(2*i+1)+4*(i+1)
            
            apples += curr*4-8*(i+1)
            i += 1
            
        return i*8
            
        