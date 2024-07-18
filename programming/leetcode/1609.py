# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = [root]
        res = []
        
        while stack:
            node = stack.pop()
            if node.right:
                if node.left:
                    stack.extend([node.right , node.left])
                else:
                    res.append(node.right.val)
                    stack.append(node.right)
            
            elif node.left:
                res.append(node.left.val)
                stack.append(node.left)
                
                
        return res