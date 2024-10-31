class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        people.sort()
        queue = ['x']*n
        
        
        for person in people:
            temp = person[1]+1	
            for k in range(n):
                
                if queue[k] == 'x' or queue[k][0] == person[0]:
                    temp -= 1
                    if temp == 0:
                        queue[k] = person 
                        break
                
                    
               
                  
                   
                    
        return queue
                
        
        
        
        