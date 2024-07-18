class Solution:
    def isPathCrossing(self, path: str) -> bool:
        class point():
            def __init__(self):
                self.x=0
                self.y=0
                self.visited=[(0,0)]
            
            def move(self,direction):
                if direction=='N':
                    self.y+=1
                elif direction=='S':
                    self.y-=1
                elif direction=='E':
                    self.x+=1
                elif direction=='W':
                    self.x-=1
                if (self.x,self.y) in self.visited:return 1
                self.visited.append((self.x,self.y))
                
        origin=point()
        for d in path:
            if origin.move(d):return 1
            
        return 0
            
                
        
        
            
        
            
        
        
        