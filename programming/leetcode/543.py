# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
              
        if not root:
            return 0
        
        def longest(node):
            if not node:
                return 0
            return 1+max(longest(node.left), longest(node.right))
        
        return max(longest(root.left)+longest(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        
        
        
        
        