# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
                
        def travel(root, s):
            if not root:
                return
            
            if not (root.right or root.left):
                res.append(s+str(root.val))
                return
            
            travel(root.left, s+f"{root.val}->")
            travel(root.right, s+f"{root.val}->")
            
        travel(root, "")
        return res
            
            