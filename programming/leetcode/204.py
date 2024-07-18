class Solution:
    def countPrimes(self, n: int) -> int:
        Table = [False] * 2 + [True] * (n-2)
        count = 0
        
        for i in range(n):
            if Table[i]:
                count +=1
                for j in range(i*i , n , i):
                    Table[j] = False

                    
        return count
                    
            
        
                
            
            
        