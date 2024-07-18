# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    @cache
    def reachable(self, node, target):
        if node is None:
            return False
        if node == target:
            return True
        return self.reachable(node.left, target) or self.reachable(node.right, target)
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if self.reachable(root.left, p) and self.reachable(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        elif self.reachable(root.right, p) and self.reachable(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)
        elif self.reachable(root, p) and self.reachable(root, q):
            return root
        
        
        
        
        
        
        
        