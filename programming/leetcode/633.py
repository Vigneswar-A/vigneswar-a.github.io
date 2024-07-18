class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        left,right = 0,int(sqrt(c))+1
        
        while left <= right:
            sum = left**2 + right**2
            
            if sum == c:
                return True
            
            elif sum > c:
                right -= 1
                
            else:
                left += 1
                
        return False
                
        