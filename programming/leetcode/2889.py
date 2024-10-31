class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        coordinates = set(map(tuple, coordinates))
        res = [0]*5
        visited = set()
        for i,j in coordinates:
            blocks = [((i-1,j-1), (i-1,j),(i,j-1),(i,j)), ((i-1,j), (i-1,j+1), (i,j), (i,j+1)), ((i, j-1), (i,j), (i+1, j-1), (i+1, j)), ((i,j),(i,j+1),(i+1,j),(i+1,j+1))]
            
            for block in blocks:
                if block in visited:
                    continue
                visited.add(block)
          
                        
                  
                    
                count = 0
                for x,y in block:
                    if 0 <= x < m and 0 <= y < n:
                        count += (x,y) in coordinates
                    else:
                        break
                else:
                    res[count] += 1
        res[0] = (m-1)*(n-1)-sum(res)
                 
        
        return res
                
                    
               
        