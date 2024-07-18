# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return inf

        res = inf
        if root.left:
            temp = root.left
            while temp.right:
                temp = temp.right
            res = min(res, (root.val - temp.val))

        if root.right:
            temp = root.right
            while temp.left:
                temp = temp.left
            res = min(res, (temp.val - root.val))

        return min(res, self.minDiffInBST(root.left), self.minDiffInBST(root.right))