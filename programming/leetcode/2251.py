class Solution:
    def numberOfWays(self, corridor: str) -> int:
        
        n = len(corridor)
        res = 1
        i = 0
        temp = 1
        scount = 0
        while i < n: 
            
            #find the first seat
            while i < n and corridor[i] != 'S':
                i += 1
            if i < n and corridor[i] == 'S':
                scount += 1
            i += 1
                
            #find the second seat
            while i < n and corridor[i] != 'S':
                i += 1
            if i < n and corridor[i] == 'S':
                scount += 1
            i += 1
            
            res *= temp
            divider = 1
            
            # for every plant we can add a divider
            while i < n and corridor[i] == 'P':
                i += 1
                divider += 1

            temp = divider

        return int(scount and scount%2 == 0) and res%(10**9 + 7)
                
                