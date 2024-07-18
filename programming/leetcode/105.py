# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        hashmap = {k:v for v,k in enumerate(inorder)}
        preorder.reverse()

        def helper(inorder=inorder):
            if not preorder or preorder[-1] not in inorder:
                return None

           
            root = TreeNode(preorder.pop())
            root.left = helper(inorder[:inorder.index(root.val)])   
            root.right = helper(inorder[inorder.index(root.val)+1:])
            
            
            return root
        
        return helper()
        
            
