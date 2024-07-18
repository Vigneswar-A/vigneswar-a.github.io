# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        
        def total(node=root):
            if node:
                return node.val + total(node.left) + total(node.right)
            return 0
        
        half = total()/2
        res = False
        def dfs(node):
            if node is None:
                return 0
            subsum = node.val + dfs(node.left) + dfs(node.right)
            
            if subsum == half:
                nonlocal res
                res = True
                
            return subsum
        dfs(root.left)
        dfs(root.right)
        
        return res
            
        
        
        

        