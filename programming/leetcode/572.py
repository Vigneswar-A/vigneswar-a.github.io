# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        @cache
        def backtrack(node = root , curr = subRoot):
            if curr == node == None:
                return True  
            elif node == None or curr == None:
                return False
            if node.val == curr.val and (backtrack(node.left , curr.left) and backtrack(node.right , curr.right)):
                return True
            else:
                return backtrack(node.left , subRoot) or backtrack(node.right, subRoot)
            
        return backtrack()
            