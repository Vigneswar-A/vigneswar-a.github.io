# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @cache
    def longestZigZag(self, root: Optional[TreeNode], dir=0, count=0) -> int:
        if root is None:
            return count-1
        
        if dir == 0:
            return max(self.longestZigZag(root.left, -1, count+1), self.longestZigZag(root.right, 1, count+1))
        
        if dir == 1:
            return max(self.longestZigZag(root.left, -1, count+1), self.longestZigZag(root.right, 1, 1))
        
        if dir == -1:
            return  max(self.longestZigZag(root.right, 1, count+1), self.longestZigZag(root.left, -1, 1))
        
        
        
        
        