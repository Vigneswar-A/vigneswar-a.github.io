class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        kx,ky = king
        result = [None]*8
        for x,y in queens:
            if x == kx and y < ky and (not result[0] or ky-y < ky-result[0][1]):
                result[0] = (x,y) 
                
            elif x == kx and y > ky and (not result[1] or y-ky < result[1][1]-ky):
                result[1] = (x,y)
                
            elif y == ky and x < kx and (not result[2] or kx-x < kx-result[2][0]):
                result[2] = (x,y)
                
            elif y == ky and x > kx and (not result[3] or x-kx < result[3][0]-kx):
                result[3] = x,y
            
            elif kx-x == ky-y and x < kx and (not result[4] or kx-x < kx-result[4][0]):                  
                result[4] = x,y
                    
            elif kx-x == ky-y and x > kx and (not result[5] or x-kx < result[5][0]-kx):
                result[5] = x,y
                    
            elif kx-x == y-ky and y < ky and (not result[6] or ky-y < ky-result[6][1]):
                result[6] = x,y
                    
            elif kx-x == y-ky and y > ky and (not result[7] or y-ky < result[7][1]-ky):
                result[7] = x,y

        return [queen for queen in result if queen]
                
            
                
                
        