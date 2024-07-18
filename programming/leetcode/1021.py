# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        @cache
        def coins(node):
            if node is None:
                return 0
            return node.val+coins(node.left)+coins(node.right)
        @cache
        def nodes(node):
            if node is None:
                return 0
            return 1+nodes(node.left)+nodes(node.right)
        
        def moves(node):
            if node is None:
                return 0
            
            left = coins(node.left)-nodes(node.left)
            right = coins(node.right)-nodes(node.right)
            return abs(left)+abs(right)+moves(node.left)+moves(node.right)
        
        
        return moves(root)
            
                
           
               
                
                
                
            
        
        
        
        