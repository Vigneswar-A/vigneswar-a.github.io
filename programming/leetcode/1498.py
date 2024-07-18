# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        stack = [(original, cloned)]
        
        while stack:
            node1,node2 = stack.pop()
            
            if node1 is None:
                continue
            
            if node1 is target:
                return node2
            
            stack.append((node1.left , node2.left))
            stack.append((node1.right, node2.right))
        