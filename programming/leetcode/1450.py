# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        @cache
        def is_uni_subtree(node):
            if not node:
                return True
            if node.val == target and is_uni_subtree(node.left) and is_uni_subtree(node.right):
                return True
            return False
        
        def helper(node):
            if node is None:
                return
            
            if node.left and is_uni_subtree(node.left) and node.left.val == target:
                node.left = None
                
            if node.right and is_uni_subtree(node.right) and node.right.val == target:
                node.right = None
                
            
            helper(node.left)
            helper(node.right)
            
        if is_uni_subtree(root):
            return None
            
        helper(root)
        return root
        