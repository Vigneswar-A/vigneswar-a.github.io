# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        
        total = 0
        node = root
        
        while node:
            
            if node.right is None:
                total += node.val
                node.val = total
                node = node.left
                
            else:
                succ = node.right
                while succ.left and succ.left != node:
                    succ = succ.left
                    
                if succ.left is None:
                    succ.left = node
                    node = node.right
                    
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node=  node.left
                
        return root