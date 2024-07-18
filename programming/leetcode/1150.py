# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        def binary_search(root, target):
            if root is None:
                return False
            if root.val == target:
                return True
            elif root.val < target:
                return binary_search(root.right, target)
            else:
                return binary_search(root.left, target)
            
        stack = [root1]
        while stack:
            node = stack.pop()
            if binary_search(root2, target-node.val):
                return True
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
                
        return False
            
        