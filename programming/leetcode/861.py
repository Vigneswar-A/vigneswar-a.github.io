class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for row in image:
            row.reverse()
            for idx in range(len(row)):
                row[idx] = (0 if row[idx] else 1)
            
                    
        return image