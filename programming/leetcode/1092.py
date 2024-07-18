# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def travel(node = root, currlowest=None, currhighest=None):
            if node is None:
                return abs(currlowest - currhighest) if currlowest is not None else 0
            if currlowest is None:
                return max(travel(node.left, node.val, node.val), travel(node.right, node.val, node.val))

            currlowest = min(node.val, currlowest)
            currhighest = max(node.val, currhighest)

            return max(travel(node.left, currlowest, currhighest), travel(node.right, currlowest, currhighest))

        return travel()

            