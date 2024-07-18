# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def get_left(root):
            if root is None:
                return None
            return root.left
        
        def get_right(root):
            if root is None:
                return None
            return root.right
        
        def get_val(root):
            if root is None:
                return 0
            return root.val
        
        if root1 == root2 == None:
            return None
        
        return TreeNode(get_val(root1)+get_val(root2), \
                        self.mergeTrees(get_left(root1), get_left(root2)), \
                        self.mergeTrees(get_right(root1), get_right(root2)))