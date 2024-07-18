# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        cand = 0
        for i in range(1, n):
            if knows(cand, i):
                cand = i
                
        if all(not knows(cand, i) and knows(i, cand) for i in range(n) if i != cand):
            return cand
        
        return -1
