# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def travel(node = root, fromleft = False):
            if not node:
                return 0
            
            if not (node.left or node.right):
                return node.val if fromleft else 0
            
            return travel(node.left, True) + travel(node.right , False)
        
        return travel()
                
            
        