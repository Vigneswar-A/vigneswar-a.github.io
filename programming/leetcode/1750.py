# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        
        def dfs(root):
            if root is not None:
                yield root.val
                yield from dfs(root.left)
                yield from dfs(root.right)

        return Counter(dfs(root1)) == Counter(dfs(root2))
        