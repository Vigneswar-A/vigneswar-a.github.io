# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        min_val = float('inf')
        res = inf
        stack = [root]
        
        while stack:
            node =  stack.pop()
            if node is None:
                continue
            diff = abs(node.val - target)
            if diff < min_val:
                min_val = diff
                res = node.val
            if target < node.val:

                stack.append(node.left)
            else:
                stack.append(node.right)
                
                
        return res
            
        
        
        
        