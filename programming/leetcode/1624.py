# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random


class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if root is None:
            return 
        
        def dfs(root, clone):
            if root is None:
                return 
            clone.val = root.val
            if root.left:
                clone.left = NodeCopy()
                dfs(root.left, clone.left)
            if root.right:
                clone.right = NodeCopy()
                dfs(root.right, clone.right)
                
        def get_eq(node, clone_node, ref_node):
            if node is None:
                return
            if node == ref_node:
                return clone_node
            return get_eq(node.left, clone_node.left, ref_node) or get_eq(node.right, clone_node.right, ref_node)
                
                
        def build_randoms(node, clone_node):
            if node is None:
                return
            
            if node.random is not None:
                clone_node.random = get_eq(root, clone_root, node.random)
            
            build_randoms(node.left, clone_node.left)
            build_randoms(node.right, clone_node.right)

        clone_root = NodeCopy()
        dfs(root, clone_root)
        build_randoms(root, clone_root)
        
        return clone_root
        