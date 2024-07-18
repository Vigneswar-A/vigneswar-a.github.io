# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0
        def travel(node , limit):
            if node.val >= limit:
                nonlocal res
                res += 1
            
            if node.left:
                travel(node.left , max(node.val , limit))
            if node.right:
                travel(node.right , max(node.val, limit))
            
        travel(root , -float('inf'))
        return res
            
                
        