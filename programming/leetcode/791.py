# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        
        if not root:
            return None, None
        elif root.val <= target:
            newroot,newchild = self.splitBST(root.right, target)
            root.right = newroot
            return root, newchild
        else:
            newroot,newchild = self.splitBST(root.left, target)
            root.left = newchild
            return newroot, root
            