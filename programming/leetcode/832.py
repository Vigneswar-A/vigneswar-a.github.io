# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def backtrack(node=root):
            
            if node is None:
                return False
            
            flag = False
            
            if node.val == 1:
                flag = True
            
            if not backtrack(node.left):
                node.left = None
            else:
                flag = True
                
            if not backtrack(node.right):
                node.right = None
            else:
                flag = True
                
            return flag
        
        if not backtrack():
            return None
        return root
                
                
                
        