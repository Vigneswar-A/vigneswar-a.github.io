class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        res = []
        for i in range(len(arr), 0, -1):
            k = arr.index(i)+1
            if k != i:
                arr[:k] = arr[:k][::-1]
                arr[:i] = arr[:i][::-1]
                res.append(k)
                res.append(i)
                
        return res
            
                
            
        