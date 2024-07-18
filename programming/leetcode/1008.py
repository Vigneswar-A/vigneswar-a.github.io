# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        
        @cache
        def dp(node, parent_has, current_has):
            if node is None:
                return 0
            
            if parent_has:
                return min(dp(node.left, 0, 0)+dp(node.right, 0, 0), dp(node.left, 1, 0)+dp(node.right, 1, 0)+1)
            
            if current_has:
                return dp(node.left, 1, 0)+dp(node.right, 1, 0)
            
            return min(dp(node.left, 1, 0)+dp(node.right, 1, 0)+1, 
                       dp(node.left, 0, 1)+dp(node.right, 0,0)+1, 
                       dp(node.left,0,0)+dp(node.right,0,1)+1, 
                       dp(node.left, 0,1)+dp(node.right,0,1)+2)
        
        return dp(root, 0, 0)
        