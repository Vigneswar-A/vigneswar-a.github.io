# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        def modify(root):
            if not root:
                return 0
            root.val = root.val + modify(root.left) + modify(root.right)
            return root.val

        mod = 10**9 + 7
        modify(root)
        total = root.val

        stack = [root]
        res = 0
        while stack:
            node = stack.pop()
            if node.left:
                res = max(res, (node.left.val)*(total-node.left.val))
                stack.append(node.left)
            if node.right:
                res = max(res, (node.right.val)*(total-node.right.val))
                stack.append(node.right)

        return res%mod
        









