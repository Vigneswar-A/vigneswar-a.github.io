class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        # Search for the row
        left,right = 0,len(matrix)      
        while left < right:
            mid = left + right >> 1
            if matrix[mid][0] > target:
                right = mid
            else:
                left = mid+1
                
        row = matrix[left-1]  
        left,right = 0,len(row)-1
        
        # Search in the row
        while left <= right:
            mid = left + right >> 1
            if row[mid] == target:
                return True
            elif row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return False
        
        
        