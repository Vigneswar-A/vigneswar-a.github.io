class Solution:
    def largestInteger(self, num: int) -> int:
        odds , evens = [] , []
        indices = []
        for n in map(int , str(num)):
            
            if n % 2:
                odds.append(n)
                indices.append(1)
            else:
                evens.append(n)
                indices.append(0)
                
        odds.sort() ; evens.sort()
        res = ''
        
        for i in indices:
            res += str((odds if i else evens).pop())
        
        return int(res)
        