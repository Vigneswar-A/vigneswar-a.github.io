# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def build_trees(left=1, right=n):
            if left > right:
                return [None]
            res = []
            for i in range(left, right+1):
                for left_node in build_trees(left, i-1):
                    for right_node in build_trees(i+1, right):
                        res.append(TreeNode(i, left_node, right_node))
            return res
        
        return build_trees()
                        
