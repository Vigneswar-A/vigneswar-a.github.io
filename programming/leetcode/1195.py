class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        people = [0]*num_people
        i = 0
        
        while candies > 0:
            people[i%num_people] += (i + 1)
            candies -= (i + 1)
            i += 1
            
            
        people[(i-1)%num_people] += candies
        
        return people
            
        