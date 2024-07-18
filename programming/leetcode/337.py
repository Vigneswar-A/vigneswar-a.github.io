# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def dp(node=root, flag=False):
            if not node:
                return 0
            
            if flag:
                return dp(node.left) + dp(node.right)
            
            return max(node.val+dp(node.left, True)+dp(node.right, True), dp(node.left)+dp(node.right))
        
        return dp()
            
            
        