# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = None
        def dfs(node, s=''):
            nonlocal res
            if node is None:
                return
            if node.left is None and node.right is None:
                s += chr(node.val+ord('a'))
                if res is None:
                    res = s[::-1]
                else:
                    res = min(res, s[::-1])
                return
            dfs(node.left, s+chr(node.val+ord('a')))
            dfs(node.right, s+chr(node.val+ord('a')))
                
        dfs(root)
        return res
            
                
        