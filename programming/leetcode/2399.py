# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:
        
        @cache
        def min_cost(node, result):
            if result == 1:
                if node.val == 2:
                    return min(min_cost(node.left, 1), min_cost(node.right, 1))
                elif node.val == 3:
                    return min_cost(node.left, 1) + min_cost(node.right, 1)
                elif node.val == 4:
                    return min(min_cost(node.left, 1)+min_cost(node.right, 0),
                               min_cost(node.left, 0)+min_cost(node.right, 1))
            else:
                if node.val == 2:
                    return min_cost(node.left, 0) + min_cost(node.right, 0)
                elif node.val == 3:
                    return min(min_cost(node.left, 0), min_cost(node.right, 0))
                elif node.val == 4:
                    return min(min_cost(node.left, 1)+min_cost(node.right, 1),
                               min_cost(node.left, 0)+min_cost(node.right, 0))
            
            if node.val == 5:
                return min_cost(node.left or node.right, not result)

            return int(node.val != result)
        
        return min_cost(root, result)
            