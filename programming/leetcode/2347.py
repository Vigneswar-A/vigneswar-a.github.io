# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        counts = Counter()
        def search(node):
            nonlocal res
            if node is None:
                return 0
            
            total = search(node.left) + search(node.right) + node.val
            counts[node] += counts[node.left] + counts[node.right] + 1
            if (total//counts[node]) == node.val:
                res += 1
            
            return total
        
        search(root)
        return res
            
            
        