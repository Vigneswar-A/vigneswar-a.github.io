class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        if (size_name := len(name)) == 1:
            return all(c == name for c in typed)
        j = 0
        count = 1
        size = len(typed)
             
        for i in range(size_name):           
            if i < size_name - 1 and name[i] == name[i + 1]:
                count += 1
                continue
            
            
            if j < size and typed[j] == name[i]:
                flag = j
                
                while j < size and typed[j] == name[i]:                
                    j += 1      
                    
                if  j - flag < count : return False     
                else: count = 1   
                    
            else:
                return False

        while j < size:
            if typed[j] != name[-1]:
                return False
            j += 1
            
        return True
                    
            
        