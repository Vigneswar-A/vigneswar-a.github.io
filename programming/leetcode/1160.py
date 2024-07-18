class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        return len(reduce(operator.__or__, (set(permutations(tiles,i)) for i in range(len(tiles)+1)))) - 1
                
        
                
                
            
                
        