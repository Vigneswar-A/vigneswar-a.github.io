class Disjoint:
    def __init__(self , n):
        self.root = [*range(n)] # Selects a leader and represents each elements leader
        self.count = 0
        self.total = n - 1
        
    def union(self , x , y):
        x , y = self.root[x] , self.root[y]
        
        if x == y:
            return False
        
        for i in range(len(self.root)):
            if self.root[i] == y:
                self.root[i] = x
        
        self.count += 1

    def is_all_connected(self):
        return self.count == self.total

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort() # Shortest time should come early
        
        people = Disjoint(n)
        
        for time , x , y in logs:
            people.union(x , y)
            if people.is_all_connected(): # If all are connected i.e they are friends
                return time    # return the time
            
        return -1 # return -1 by default
        