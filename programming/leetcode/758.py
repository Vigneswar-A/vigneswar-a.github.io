"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        nodes = []
        
        def dfs(node):
            if not node:
                return None
            nodes.append(node)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        nodes.sort(key=lambda node:node.val)
        
        size = len(nodes)
        head = nodes[0]
        for i in range(len(nodes)):
            nodes[i].left = nodes[i-1]
            nodes[i].right = nodes[(i+1)%size]
        
        head.left = nodes[-1]
        nodes[-1].right = head
        return head
        
            