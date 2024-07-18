# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        hashmap = {k:v for v,k in enumerate(inorder)}
        
        def helper(inorder=inorder):
            if not postorder or postorder[-1] not in inorder:
                return None

           
            root = TreeNode(postorder.pop())
            root.right = helper(inorder[inorder.index(root.val)+1:])
            root.left = helper(inorder[:inorder.index(root.val)])   
            
            return root
        
        return helper()
        