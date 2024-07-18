class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        def get_overlap(x, y, mat1, mat2):

            count1 = count2 = 0
            for x1,x2 in zip(range(n), range(x, n)):
                for y1,y2 in zip(range(n), range(y, n)):
                    if mat1[x1][y1] and mat2[x2][y2]:
                        count1 += 1
                    if mat1[x1][y2] and mat2[x2][y1]:
                        count2 += 1
                        
            return max(count1, count2)
        
        res = 0
        for i in range(n):
            for j in range(n):
                res = max(res, 
                          get_overlap(i , j , img1, img2),
                          get_overlap(i , j , img2, img1)
                         )
                
        return res
        