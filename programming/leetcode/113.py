# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        path = [root.val]
        
        def backtrack(node=root, total=root.val):            
            if not (node.left or node.right):
                if total == targetSum:
                    res.append(path[:])
                return
            
            if node.left:
                path.append(node.left.val)
                backtrack(node.left, total+node.left.val)
                path.pop()
                
            if node.right:
                path.append(node.right.val)
                backtrack(node.right, total+node.right.val)
                path.pop()
                
            return
    
        backtrack()
        return res
            