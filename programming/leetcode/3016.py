# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countGreatEnoughNodes(self, root: Optional[TreeNode], k: int) -> int:
        from sortedcontainers import SortedList
        
        res = 0
        def traverse(node):
            nonlocal res
            if node is None:
                return SortedList()
            
            nums = (traverse(node.left)+traverse(node.right))
            res += (nums.bisect_left(node.val) >= k)
            return (nums[:k] + SortedList([node.val]))
        
        traverse(root)
        return res
                
                
                