# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        @cache
        def get_sum_linear(root):
            if not root:
                return 0
            return max(max(get_sum_linear(root.left), get_sum_linear(root.right)) + root.val, 0)

        def get_max_path(root):
            if not root:
                return -inf
            return max(
                    root.val + get_sum_linear(root.left) + get_sum_linear(root.right),
                    get_max_path(root.left),
                    get_max_path(root.right),
                    root.val
                )

        return get_max_path(root)

        
