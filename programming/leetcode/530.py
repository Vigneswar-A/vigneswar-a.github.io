# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        
        temp = []
        res = float('inf')
        prev = -float('inf')
        def inorder(root):
            if root is None:
                return root
            
            inorder(root.left)
            nonlocal res,prev
            res = min(res, root.val-prev)
            prev = root.val
            inorder(root.right)
        inorder(root)
        return res
