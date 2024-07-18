class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
       
        rqueue = deque()
        dqueue = deque()
        banned = set()
        
        
        
        for i,c in enumerate(senate):
            if c == 'R':
                rqueue.append(i)
            else:
                dqueue.append(i)
                
        
        i = -1
        while True:
           
            
            


            

            i = (i+1)%n
            
  
            if i in banned:
                continue 
            c = senate[i]
            if c == 'R':
                if not dqueue:
                    return 'Radiant'
                rqueue.append(rqueue.popleft())
                banned.add(dqueue.popleft())
                
            else:
                if not rqueue:
                    return 'Dire'
                dqueue.append(dqueue.popleft())
                banned.add(rqueue.popleft())
                
            
          
      
                
        
        
 
        
        

        