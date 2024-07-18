# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        
        stack = []
        sum = 0 
        node = root
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.right    
            
            node = stack.pop()
            sum += node.val
            node.val = sum
            node = node.left
                     
        return  root
            
        