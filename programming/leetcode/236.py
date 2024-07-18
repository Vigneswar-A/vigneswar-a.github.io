# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans = root
        
        @cache
        def has_node(root, node):
            if root is None:
                return False
            
            if root == node:
                return True
            
            return has_node(root.left, node) or has_node(root.right, node)
        
        
        def dfs(root):
            if root is None:
                return False
            
            if has_node(root.left, p) and has_node(root.left, q):
                return dfs(root.left)
            if has_node(root.right, p) and has_node(root.right, q):
                return dfs(root.right)
            
            return root
        
        return dfs(root)
        