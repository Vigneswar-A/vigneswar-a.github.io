class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        
        left = up = inf
        right = down = -inf
        
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == "1":
                    left = min(left, j)
                    right = max(right, j)
                    down = max(down, i)
                    up = min(up, i)

        return (right-left+1)*(down-up+1)
                
                
        