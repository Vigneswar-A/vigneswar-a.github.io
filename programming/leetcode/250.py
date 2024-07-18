# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = 0
        def travel(node):   
            nonlocal count
            if node.left and node.right:
                leftval = travel(node.left)
                rightval = travel(node.right)
                if leftval == rightval == node.val:
                    count += 1
                    return node.val    
                    
            elif node.left:
                if node.val == travel(node.left):
                    count += 1
                    return node.val
                    
            elif node.right:
                if node.val == travel(node.right):
                    count += 1
                    return node.val
            else:    
                count += 1
                return node.val
        
        travel(root)
        return count
        