class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        i = 0
        water = capacity
        step = 0
        end = len(plants)
        
        while i < end:
            if water >= plants[i]:
                water -= plants[i]
                i += 1
                
            else:
                water = capacity
                step += 2*i - 1
                
            step += 1
                
        return step
        