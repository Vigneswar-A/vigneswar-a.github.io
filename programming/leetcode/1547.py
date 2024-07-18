class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        destination=dict(paths)   
        current=paths[0][0]
        
        while current in destination:
            current=destination[current]
            
        return current 