# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def travel(node=root, total=0):
            if not node:
                return
            if not (node.left or node.right):
                return total+node.val == targetSum
            
            return travel(node.left, total+node.val) or travel(node.right, total+node.val)
        
        return travel()
        