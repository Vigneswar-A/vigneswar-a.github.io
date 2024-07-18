# Definition for a street.
# class Street:
#     def closeDoor(self):
#         pass
#     def isDoorOpen(self):
#         pass
#     def moveRight(self):
#         pass
class Solution:
    def houseCount(self, street: Optional['Street'], k: int) -> int:
        count = 0
        
        while True:
            for i in range(k):
                if street.isDoorOpen():
                    break
                street.moveRight()
            else:
                return count
                
            count = 1
            street.moveRight()
            
            while not street.isDoorOpen():
                count += 1
                street.moveRight()
                
            street.closeDoor()

        return count
            
        
            
    
        