class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        Map={}
        i=1
        for n in sorted(arr):
            if n in Map:
                continue
            
            Map[n]=i
            i+=1
        
        return map(Map.get,arr)
            
        
        
            
               
        
            
        