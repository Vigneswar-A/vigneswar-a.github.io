# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        def is_bst(node, lower=-inf, upper=inf):
            if node is None:
                return 0
            if node.val >= upper or node.val <= lower:
                return -float(inf)
            return is_bst(node.left, lower, node.val)+is_bst(node.right, node.val, upper)+1
        
        
        stack = [root]
        res = 0
        while stack:
            node = stack.pop()
            if not node:
                continue
                
            res = max(res, is_bst(node))
            stack.extend([node.left, node.right])
            
        return res

            
            






            
        
        


            
            
