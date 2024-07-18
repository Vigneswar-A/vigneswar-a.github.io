# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        TreeNode.__repr__ = lambda self: str(self.val)
        def in_order(node):
            if node is None:
                return
            yield from in_order(node.left)
            yield node
            yield from in_order(node.right)
            
        nodes = list(in_order(root))
        
        def build(nodes):
            if not nodes:
                return None
            mid = len(nodes)//2
            root = nodes[mid]
            left = nodes[:mid]
            right = nodes[mid+1:]
            root.left = build(left)
            root.right = build(right)
            return root 
        return build(nodes)
            