class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        a,d=arr[1],arr[1]-arr[0]
        
        for i in arr[2:]:
            if i-a!=d:
                return 
            a=i
        
        return ...
        
        
        