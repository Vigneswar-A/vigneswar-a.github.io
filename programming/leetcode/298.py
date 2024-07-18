# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def dp(node=root, prev=float('inf'), score=1):
            if not node:
                return score
            
            if node.val == prev+1:
                return max(dp(node.left, node.val, score+1), dp(node.right, node.val, score+1))
            
            return max(dp(node.left , node.val), dp(node.right, node.val), score)
            
        return dp()
        