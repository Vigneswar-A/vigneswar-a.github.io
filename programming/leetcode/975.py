# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        if not root:
            return 0

        temp = 0
        if root.val < low:
            temp += self.rangeSumBST(root.right, low, high)

        elif root.val > high:
            temp += self.rangeSumBST(root.left, low, high)

        else:
            temp += root.val+self.rangeSumBST(root.right, low, high)+self.rangeSumBST(root.left, low, high)

        return temp

        


        return 0