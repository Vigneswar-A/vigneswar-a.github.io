class Solution:
    def canBeIncreasing(self, array: List[int]) -> bool:
        flag=False
        for i in range(len(array)-1):
            if array[i]<array[i+1]:
                continue
            flag=True
            temp=array[:]
            array.pop(i)
            temp.pop(i+1)
            break
            
        if not flag:
            return True
        
        for i in range(len(array)-1):
            if array[i]<array[i+1]:
                continue
            flag=False
            break
            
        if flag:
            return True
        
        for i in range(len(temp)-1):
            if temp[i]<temp[i+1]:
                continue
            return False
        
        return True
        
        
    
            
        
        
            
        