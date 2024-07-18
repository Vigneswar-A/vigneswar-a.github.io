class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.x = 0
        self.y = 0
        self.size = 0
        self.directions = {'U' : (0,-1) , 'D' : (0,1) , 'R' : (1,0) , 'L' : (-1,0)}
        self.body = []
        

    def move(self, direction: str) -> int:
        dx,dy = self.directions[direction]
        self.x += dx
        self.y += dy
        
        if not (0 <= self.x < self.width and 0 <= self.y < self.height) or (self.x , self.y) in self.body:
            return -1
        
        self.body.append((self.x , self.y))
        
        if self.food and self.food[0] == [self.y , self.x]:
            self.food.pop(0)
            self.size += 1
        else:
            self.body.pop(0)
            
        return self.size
        
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)