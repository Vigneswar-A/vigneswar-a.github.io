# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        res = 0
        stack = [(root, 0)]
        while stack:
            node,val = stack.pop()
            if node is None:
                res += val
                continue

            if node.left:
                stack.append((node.left, (val << 1) + node.val))
            if node.right:
                stack.append((node.right, (val << 1) + node.val))

            if not (node.left or node.right):
                res += (val << 1) + node.val

        return res
            
