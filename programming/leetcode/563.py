# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        def tilt(root):
            if root is None:
                return 0
            return tilt(root.left) + tilt(root.right) + abs(sum(root.left) - sum(root.right))
        
        @cache
        def sum(root):
            if root is None:
                return 0
            return root.val+sum(root.left)+sum(root.right)
        
        return tilt(root)
        
        
        