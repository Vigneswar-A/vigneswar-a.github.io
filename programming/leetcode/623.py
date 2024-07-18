# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            root = TreeNode(val, root, None)
            return root
        
        def add(node, currdepth=2):
            if not node:
                return
            if currdepth == depth:
                node.left = TreeNode(val, node.left)
                node.right = TreeNode(val, None, node.right)
                return
            
            add(node.left, currdepth+1)
            add(node.right, currdepth+1)
            
        add(root)
        return root
                
            

        