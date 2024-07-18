# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def get_string(node=root, s=''):
            if not node:
                return ""
            s += str(node.val)
            if node.left:
                s += f"({get_string(node.left)})" + (f"({get_string(node.right)})" if node.right else '')
            elif node.right:
                s += f"()({get_string(node.right)})"
            return s

        return get_string()

