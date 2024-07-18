# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return 
        
        if root.val == key:
            if not (root.left or root.right):
                return None

            if root.left and root.right:
                temp = root.left
                while temp.right:
                    temp = temp.right
                root.val = temp.val
                root.left = self.deleteNode(root.left, temp.val)
                return root

            return (root.left or root.right)
            
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
        