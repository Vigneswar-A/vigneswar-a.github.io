# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        @cache
        def get_depth(root):
            if not root:
                return 0
            
            return 1+max(get_depth(root.left), get_depth(root.right))
        
        if not root:
            return True
        
        if abs(get_depth(root.left) - get_depth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        return False