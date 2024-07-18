# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        counts = Counter()
        res = 0
        
        def backtrack(node = root):
            if not (node.left or node.right):
                counts[node.val] += 1
                if sum(i%2 for i in counts.values()) < 2:
                    nonlocal res
                    res += 1
                counts[node.val] -= 1
                return None
                    
            counts[node.val] += 1
            if node.left:
                backtrack(node.left)
            if node.right:
                backtrack(node.right)
            counts[node.val] -= 1
            
        backtrack()
        return res
        
        