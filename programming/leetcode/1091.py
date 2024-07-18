# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        def update_sum(root):
            if root is None:
                return 0
            root.val += update_sum(root.left) + update_sum(root.right)
            return root.val
        
        def update_length(root):
            if root is None:
                return 0
            root.size = 1
            root.size += update_length(root.left) + update_length(root.right)
            return root.size
        
        update_sum(root)
        update_length(root)
        
        res = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            res = max(res, node.val/node.size)
            stack.append(node.left)
            stack.append(node.right)

        return res
        
        
    
        