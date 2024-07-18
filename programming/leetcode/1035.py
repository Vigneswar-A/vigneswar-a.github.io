# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        xparent = yparent = xlevel = ylevel = None

        def get_level(node=root, depth=0, parent=None):
            if node is None:
                return 
            nonlocal xlevel, ylevel, xparent, yparent
            if node.val == x:
                xlevel = depth
                xparent = parent
            elif node.val == y:
                ylevel = depth
                yparent = parent

            if xlevel is not None and ylevel is not None:
                return

            get_level(node.left, depth+1, node.val)
            get_level(node.right, depth+1, node.val)

        get_level()
        return xlevel == ylevel and xparent != yparent
