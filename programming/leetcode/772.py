"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        def build(i=0, j=0, size=n):
            if len(set(grid[x+i][y+j] for x in range(size) for y in range(size))) == 1:
                return Node(grid[i][j], 1, None, None, None)
            root = Node(1, 0)
            root.topLeft = build(i, j, size//2)
            root.topRight = build(i, j+size//2, size//2)
            root.bottomLeft = build(i+size//2, j, size//2)
            root.bottomRight = build(i+size//2, j+size//2, size//2)
            return root
        
        return build()
            
                
                
        