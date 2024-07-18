class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        
        Jumbo = (tomatoSlices - 2*cheeseSlices) / 2
        
        Small = cheeseSlices - Jumbo
        
        if int(Jumbo) == Jumbo >= 0 and int(Small) == Small >= 0:
            return [int(Jumbo), int(Small)]
        
        return []
        
        