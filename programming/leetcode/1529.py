class Solution:
    def maxDiff(self, num: int) -> int:
        
        size = len(str(num))
        max_val = min_val = str(num)
        
        i = 0
        while i < size and max_val[i] == '9':
            i += 1    
        if i < size:
            max_val = max_val.replace(max_val[i], '9')
        
        i = 0
        while i < size and (min_val[i] == '1' or min_val[i] == '0'):
            i += 1
        if i < size:
            min_val = min_val.replace(min_val[i], '0' if i else '1')

        return int(max_val) - int(min_val)
                
        