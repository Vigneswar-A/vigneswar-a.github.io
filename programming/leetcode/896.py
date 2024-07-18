# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        @cache
        def depth(root):
            if root is None:
                return 0
            return max(depth(root.left), depth(root.right)) + 1
        
        def dp(root):
            if root is None:
                return
            
            if depth(root.left) > depth(root.right):
                return dp(root.left)
            
            if depth(root.right) > depth(root.left):
                return dp(root.right)

            return root
        
        return dp(root)
        
        
        